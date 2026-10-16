PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS schema_migrations (
    version INTEGER PRIMARY KEY,
    applied_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS sources (
    source_id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    creator TEXT NOT NULL,
    publication TEXT NOT NULL,
    source_kind TEXT NOT NULL,
    source_url TEXT,
    local_path TEXT,
    rights_status TEXT NOT NULL CHECK (
        rights_status IN ('unknown', 'metadata-only', 'open-license',
                          'permission-granted', 'public-domain', 'project-original')
    ),
    rights_reference TEXT NOT NULL DEFAULT '',
    citation TEXT NOT NULL,
    extraction_status TEXT NOT NULL,
    CHECK (source_url IS NULL OR source_url = '' OR
           source_url LIKE 'https://%' OR source_url LIKE 'http://%'),
    CHECK (rights_status NOT IN ('open-license', 'permission-granted', 'public-domain')
           OR rights_reference <> '')
);

CREATE TABLE IF NOT EXISTS concepts (
    concept_id TEXT PRIMARY KEY,
    concept_name TEXT NOT NULL,
    domain TEXT NOT NULL CHECK (domain <> ''),
    topic_id TEXT UNIQUE,
    summary TEXT NOT NULL,
    reference TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS concept_links (
    source_id TEXT NOT NULL REFERENCES concepts(concept_id),
    target_id TEXT NOT NULL REFERENCES concepts(concept_id),
    relation TEXT NOT NULL CHECK (relation IN ('requires', 'uses_math')),
    PRIMARY KEY (source_id, target_id, relation),
    CHECK (source_id <> target_id)
);

CREATE TABLE IF NOT EXISTS concept_sources (
    concept_id TEXT NOT NULL REFERENCES concepts(concept_id),
    source_id TEXT NOT NULL REFERENCES sources(source_id),
    source_locator TEXT NOT NULL,
    relation TEXT NOT NULL CHECK (
        relation IN ('related-resource', 'defines', 'supports', 'illustrates', 'uses')
    ),
    review_status TEXT NOT NULL CHECK (
        review_status IN ('draft', 'needs-review', 'verified', 'disputed')
    ),
    reviewer TEXT NOT NULL DEFAULT '',
    notes TEXT NOT NULL DEFAULT '',
    PRIMARY KEY (concept_id, source_id, source_locator),
    CHECK (review_status <> 'verified' OR reviewer <> '')
);

CREATE TABLE IF NOT EXISTS papers (
    paper_id TEXT PRIMARY KEY,
    exam TEXT NOT NULL,
    exam_name TEXT NOT NULL,
    year INTEGER NOT NULL CHECK (year BETWEEN 1900 AND 2200),
    session TEXT NOT NULL,
    paper_name TEXT NOT NULL,
    subject TEXT NOT NULL,
    source_id TEXT NOT NULL REFERENCES sources(source_id),
    review_status TEXT NOT NULL CHECK (
        review_status IN ('needs-source-review', 'verified', 'disputed')
    ),
    notes TEXT NOT NULL DEFAULT ''
);

CREATE TABLE IF NOT EXISTS questions (
    question_id TEXT PRIMARY KEY,
    paper_id TEXT NOT NULL REFERENCES papers(paper_id),
    source_id TEXT NOT NULL REFERENCES sources(source_id),
    question_locator TEXT NOT NULL,
    question_format TEXT NOT NULL,
    difficulty TEXT NOT NULL DEFAULT '',
    marks REAL,
    topic_id TEXT NOT NULL REFERENCES concepts(topic_id),
    review_status TEXT NOT NULL CHECK (
        review_status IN ('draft', 'needs-review', 'verified', 'disputed')
    ),
    answer_verified INTEGER NOT NULL DEFAULT 0 CHECK (answer_verified IN (0, 1)),
    reviewer TEXT NOT NULL DEFAULT '',
    reviewed_at TEXT NOT NULL DEFAULT '',
    notes TEXT NOT NULL DEFAULT '',
    CHECK (review_status <> 'verified' OR (reviewer <> '' AND reviewed_at <> ''))
);

CREATE TABLE IF NOT EXISTS question_concepts (
    question_id TEXT NOT NULL REFERENCES questions(question_id) ON DELETE CASCADE,
    concept_id TEXT NOT NULL REFERENCES concepts(concept_id),
    relation TEXT NOT NULL CHECK (relation IN ('assesses', 'requires', 'uses')),
    confidence REAL NOT NULL CHECK (confidence >= 0 AND confidence <= 1),
    review_status TEXT NOT NULL CHECK (
        review_status IN ('draft', 'needs-review', 'verified', 'disputed')
    ),
    reviewer TEXT NOT NULL DEFAULT '',
    source_locator TEXT NOT NULL DEFAULT '',
    notes TEXT NOT NULL DEFAULT '',
    PRIMARY KEY (question_id, concept_id, relation),
    CHECK (review_status <> 'verified' OR (reviewer <> '' AND source_locator <> ''))
);

CREATE TABLE IF NOT EXISTS problem_models (
    problem_id TEXT PRIMARY KEY,
    question_id TEXT UNIQUE REFERENCES questions(question_id) ON DELETE CASCADE,
    source_id TEXT NOT NULL REFERENCES sources(source_id),
    concept_id TEXT NOT NULL REFERENCES concepts(concept_id),
    model_type TEXT NOT NULL,
    inputs_json TEXT NOT NULL CHECK (json_valid(inputs_json)),
    expected_outputs_json TEXT CHECK (
        expected_outputs_json IS NULL OR json_valid(expected_outputs_json)
    ),
    assumptions_json TEXT NOT NULL CHECK (json_valid(assumptions_json)),
    unit_system TEXT NOT NULL,
    review_status TEXT NOT NULL CHECK (
        review_status IN ('draft', 'needs-review', 'verified', 'disputed')
    )
);

CREATE TABLE IF NOT EXISTS engine_runs (
    run_id TEXT PRIMARY KEY,
    problem_id TEXT NOT NULL REFERENCES problem_models(problem_id),
    engine_name TEXT NOT NULL,
    engine_version TEXT NOT NULL,
    input_hash TEXT NOT NULL,
    result_json TEXT NOT NULL CHECK (json_valid(result_json)),
    check_status TEXT NOT NULL CHECK (
        check_status IN ('passed', 'failed', 'not-run')
    ),
    created_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS lessons (
    lesson_id TEXT PRIMARY KEY,
    question_id TEXT REFERENCES questions(question_id),
    problem_id TEXT REFERENCES problem_models(problem_id),
    title TEXT NOT NULL,
    audience TEXT NOT NULL,
    language TEXT NOT NULL,
    duration_seconds INTEGER NOT NULL CHECK (duration_seconds > 0),
    ir_version INTEGER NOT NULL CHECK (ir_version > 0),
    ir_json TEXT NOT NULL CHECK (json_valid(ir_json)),
    editorial_status TEXT NOT NULL CHECK (
        editorial_status IN ('draft', 'approved', 'rejected')
    ),
    physics_status TEXT NOT NULL CHECK (
        physics_status IN ('pending', 'approved', 'rejected')
    ),
    design_status TEXT NOT NULL CHECK (
        design_status IN ('pending', 'approved', 'rejected')
    ),
    release_status TEXT NOT NULL CHECK (
        release_status IN ('pending', 'approved', 'rejected')
    ),
    render_status TEXT NOT NULL CHECK (
        render_status IN ('pending', 'rendered', 'reviewed', 'rejected')
    ),
    created_at TEXT NOT NULL,
    CHECK (question_id IS NOT NULL OR problem_id IS NOT NULL)
);

CREATE TABLE IF NOT EXISTS lesson_concepts (
    lesson_id TEXT NOT NULL REFERENCES lessons(lesson_id) ON DELETE CASCADE,
    concept_id TEXT NOT NULL REFERENCES concepts(concept_id),
    role TEXT NOT NULL CHECK (role IN ('teaches', 'prerequisite', 'uses_math')),
    PRIMARY KEY (lesson_id, concept_id, role)
);

CREATE TABLE IF NOT EXISTS lesson_scenes (
    lesson_id TEXT NOT NULL REFERENCES lessons(lesson_id) ON DELETE CASCADE,
    scene_id TEXT NOT NULL,
    sequence_number INTEGER NOT NULL CHECK (sequence_number > 0),
    scene_type TEXT NOT NULL,
    purpose TEXT NOT NULL,
    visual_spec_json TEXT NOT NULL CHECK (json_valid(visual_spec_json)),
    narration TEXT NOT NULL DEFAULT '',
    approval_status TEXT NOT NULL CHECK (
        approval_status IN ('draft', 'approved', 'rejected')
    ),
    PRIMARY KEY (lesson_id, scene_id),
    UNIQUE (lesson_id, sequence_number)
);

CREATE INDEX IF NOT EXISTS idx_questions_topic_review
    ON questions(topic_id, review_status);
CREATE INDEX IF NOT EXISTS idx_papers_exam_year
    ON papers(exam, year);
CREATE INDEX IF NOT EXISTS idx_links_target_relation
    ON concept_links(target_id, relation);
CREATE INDEX IF NOT EXISTS idx_concept_sources_source
    ON concept_sources(source_id);
CREATE INDEX IF NOT EXISTS idx_runs_problem_created
    ON engine_runs(problem_id, created_at);

CREATE VIEW IF NOT EXISTS question_knowledge_map AS
SELECT
    q.question_id,
    q.paper_id,
    q.question_locator,
    q.topic_id,
    q.review_status AS question_review_status,
    qc.concept_id,
    c.concept_name,
    c.domain,
    qc.relation,
    qc.confidence,
    qc.review_status AS link_review_status
FROM questions AS q
LEFT JOIN question_concepts AS qc ON qc.question_id = q.question_id
LEFT JOIN concepts AS c ON c.concept_id = qc.concept_id;

CREATE VIEW IF NOT EXISTS exam_question_records AS
SELECT
    q.question_id,
    p.exam,
    p.exam_name,
    p.year,
    p.session,
    p.paper_id,
    p.subject,
    q.topic_id,
    s.title AS source_name,
    s.source_url,
    s.source_kind AS source_type,
    s.rights_status,
    s.rights_reference,
    q.question_locator,
    q.question_format,
    q.difficulty,
    q.marks,
    CAST(q.answer_verified AS TEXT) AS answer_verified,
    q.review_status,
    q.reviewer,
    q.reviewed_at,
    q.notes
FROM questions AS q
JOIN papers AS p ON p.paper_id = q.paper_id
JOIN sources AS s ON s.source_id = q.source_id
WHERE p.exam IN ('neet', 'jee-main', 'jee-advanced');

CREATE TRIGGER IF NOT EXISTS verified_question_requires_public_source
BEFORE INSERT ON questions
WHEN NEW.review_status = 'verified'
 AND NOT EXISTS (
    SELECT 1 FROM sources AS s
    JOIN papers AS p ON p.source_id = s.source_id
    WHERE s.source_id = NEW.source_id
      AND p.paper_id = NEW.paper_id
      AND p.review_status = 'verified'
      AND s.source_url IS NOT NULL
      AND s.source_url <> ''
 )
BEGIN
    SELECT RAISE(ABORT, 'verified questions require a verified paper and traceable HTTP source URL');
END;

CREATE TRIGGER IF NOT EXISTS updated_verified_question_requires_public_source
BEFORE UPDATE OF review_status, source_id, paper_id ON questions
WHEN NEW.review_status = 'verified'
 AND NOT EXISTS (
    SELECT 1 FROM sources AS s
    JOIN papers AS p ON p.source_id = s.source_id
    WHERE s.source_id = NEW.source_id
      AND p.paper_id = NEW.paper_id
      AND p.review_status = 'verified'
      AND s.source_url IS NOT NULL
      AND s.source_url <> ''
 )
BEGIN
    SELECT RAISE(ABORT, 'verified questions require a verified paper and traceable HTTP source URL');
END;

CREATE TRIGGER IF NOT EXISTS question_source_must_match_paper
BEFORE INSERT ON questions
WHEN NOT EXISTS (
    SELECT 1 FROM papers
    WHERE paper_id = NEW.paper_id AND source_id = NEW.source_id
)
BEGIN
    SELECT RAISE(ABORT, 'question source_id must match its paper source_id');
END;

CREATE TRIGGER IF NOT EXISTS updated_question_source_must_match_paper
BEFORE UPDATE OF paper_id, source_id ON questions
WHEN NOT EXISTS (
    SELECT 1 FROM papers
    WHERE paper_id = NEW.paper_id AND source_id = NEW.source_id
)
BEGIN
    SELECT RAISE(ABORT, 'question source_id must match its paper source_id');
END;

CREATE TRIGGER IF NOT EXISTS verified_paper_source_url_preserved
BEFORE UPDATE OF source_url ON sources
WHEN (NEW.source_url IS NULL OR NEW.source_url = '')
 AND EXISTS (
    SELECT 1 FROM papers p
    JOIN questions q ON q.paper_id = p.paper_id
    WHERE p.source_id = OLD.source_id AND p.review_status = 'verified'
      AND q.review_status = 'verified'
 )
BEGIN
    SELECT RAISE(ABORT, 'cannot remove source URL while verified questions depend on it');
END;

CREATE TRIGGER IF NOT EXISTS verified_paper_requires_traceable_source
BEFORE INSERT ON papers
WHEN NEW.review_status = 'verified'
 AND NOT EXISTS (
    SELECT 1 FROM sources
    WHERE source_id = NEW.source_id AND source_url IS NOT NULL AND source_url <> ''
 )
BEGIN
    SELECT RAISE(ABORT, 'verified papers require a traceable HTTP source URL');
END;

CREATE TRIGGER IF NOT EXISTS updated_verified_paper_requires_traceable_source
BEFORE UPDATE OF review_status, source_id ON papers
WHEN NEW.review_status = 'verified'
 AND NOT EXISTS (
    SELECT 1 FROM sources
    WHERE source_id = NEW.source_id AND source_url IS NOT NULL AND source_url <> ''
 )
BEGIN
    SELECT RAISE(ABORT, 'verified papers require a traceable HTTP source URL');
END;

CREATE TRIGGER IF NOT EXISTS paper_source_change_preserves_question_source
BEFORE UPDATE OF source_id ON papers
WHEN EXISTS (
    SELECT 1 FROM questions
    WHERE paper_id = NEW.paper_id AND source_id <> NEW.source_id
)
BEGIN
    SELECT RAISE(ABORT, 'paper source_id cannot change while linked questions use another source');
END;
