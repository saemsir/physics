# studio_engine/kernel.py
"""Kernel: classify -> route -> dispatch -> remember (3 memory tiers)."""
ROUTES = [
    ("physics:",  "physics_engine"),   ("math:",     "math_engine"),
    ("exam:",     "exam_engine"),      ("content:",  "content_engine"),
    ("matrix.",   "matrix_pipeline"),  ("video.",    "video_learning"),
]
def route(request_text, graph):                 # attention = concept-graph match
    hits = match_concepts(request_text, graph)  # your existing matcher
    for prefix, engine in ROUTES:
        if any(c.startswith(prefix.split(":")[0]) for c in hits):
            return engine
    return "content_engine"                     # default scheduler

def remember(tier, key, value):                 # working / episodic / semantic
    # working  = RUNNER_TEMP run state; episodic = data/repo_learner_state.json
    # semantic = saemphysics.sqlite knowledge graph
    ...
