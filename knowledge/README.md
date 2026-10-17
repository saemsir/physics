# Physics and mathematics concept graph

The graph is a small, version-controlled index connecting the Physics topic
IDs in `../data/physics_topics.csv` to original concept summaries, mathematics
tools, and prerequisites:

- `concepts.csv`: one stable node per idea, with a lowercase domain identifier
  (for example `mathematics`, `physics`, or future `computer_science` nodes).
- `links.csv`: directed `requires` and `uses_math` edges.
- `../data/exam_question_metadata.csv`: source-linked records attach to their
  Physics concept through `topic_id`; the relation can be followed to its
  mathematical tools.
- `../data/concept_sources.csv`: source locators attach books/courses to concepts
  without implying permission to reproduce their contents.
- Chemistry concepts are also included as a starter vocabulary for the local
  matrix index; they do not imply a reviewed exam syllabus or an implemented
  chemistry solver.
- `solution_routes.csv` lists typed-input solver capabilities and the planned
  or available visual/narration approaches for concepts. Add a route only
  when its engine capability exists and its required input contract is known.

Check and query a mapping from the repository root:

```bash
python -m exam_engine map-topic --topic kinematics
python -m exam_engine map-topic --topic electrostatics
python -m exam_engine map-topic --topic oscillations_waves
```

The graph loader checks stable IDs, complete one-to-one Physics-topic
coverage, extensible domain identifiers, relation types, missing nodes,
prerequisite cycles, and that every mathematics concept is connected from a
non-mathematics concept. Tests exercise the same
checks. A question is not automatically linked to concepts merely because a
tag exists: a human must verify its source and topic tag in the question
metadata ledger.

## Source and syllabus coverage

The Strang material in this repository identifies itself as MIT OpenCourseWare
18.085, *Computational Science and Engineering I*, Fall 2008. Chapter 1 is
*Applied Linear Algebra*; the course material also includes Fourier series and
integrals. The graph cites those high-level course sections and stores short,
original summaries rather than book prose or figures. The course listing is
at <https://ocw.mit.edu/courses/18-085-computational-science-and-engineering-i-fall-2008/>.
Check the terms of the exact OCW resource before redistributing its files.

## Applied linear algebra design principles

The implementation takes broad computational lessons from Chapter 1 rather
than copying its exposition:

- Treat a matrix as a transformation of meaningful state variables, not just
  a table of numbers. The solver reports what it computed and a residual;
  the calling physics model must still define what each component means.
- Check dimensions, rank-sensitive cases, pivot behavior, and residuals.
  A singular or numerically suspect system is an explicit failure, not a
  fabricated answer.
- Select algorithms that fit the actual structure. The current reference
  solver is for small dense systems; exploiting sparse or banded structure is
  a future, separately tested optimization.
- Connect representation to the observable: vectors, matrix actions, and
  Fourier components are useful only when their mapping to a physical model
  and its units is clear.
- Test known solutions and edge cases; numerical output is evidence to check,
  never an automatic proof of the physics.

The graph is a starter map, not a certified transcription of NEET or JEE
syllabi. Each Physics node therefore marks its official syllabus reference as
`needs-official-version`. Before asserting exam-specific alignment, add a
versioned official syllabus source, exact section reference, year range, and
human review. Avoid deriving exam relevance from question frequency alone.

Add a node with a stable ID, concise original explanation, a precise topic
cross-reference, and source provenance. Add only relationships that have been
reviewed for the intended curriculum. Keep full copyrighted question wording,
solutions, figures, and book extracts out of the public graph.
