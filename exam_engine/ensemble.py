# exam_engine/ensemble.py
import math
from .engine import rolling_origin_brier, predict_mix   # your existing internals

def ensemble_forecast(papers, catalog, as_of, grid_hl=(4, 8, 16), grid_alpha=(0.5, 1.0, 2.0), beta=8.0):
    weights, mixes = [], []
    for hl in grid_hl:
        for alpha in grid_alpha:
            loss = rolling_origin_brier(papers, catalog, half_life=hl, prior_mass=alpha)
            weights.append(math.exp(-beta * loss))
            mixes.append(predict_mix(papers, catalog, as_of, half_life=hl, prior_mass=alpha))
    Z = sum(weights) or 1.0
    K = len(catalog)
    return [sum(w * mx[t] for w, mx in zip(weights, mixes)) / Z for t in range(K)], \
           [{"half_life": hl, "prior_mass": al, "weight": round(w / Z, 4)}
            for (hl, al), w in zip(((h, a) for h in grid_hl for a in grid_alpha), weights)]
