#!/usr/bin/env python3
"""Discretized least-action paths: S[q] = sum_i [T - V] dt, stationary under
interior variations. Endpoints fixed; Euler-Lagrange residual reported."""
from __future__ import annotations
import argparse, json, math

POTENTIALS = {
    "free":        lambda x, p: 0.0,
    "gravity":     lambda x, p: p.get("m", 1.0) * p.get("g", 9.8) * x,
    "harmonic":    lambda x, p: 0.5 * p.get("k", 1.0) * x * x,
    "double_well": lambda x, p: p.get("a", 1.0) * (x * x - 1.0) ** 2,
}

def _dV(pot, x, p, h=1e-6):
    return (pot(x + h, p) - pot(x - h, p)) / (2 * h)

def action(q, dt, pot, p, m=1.0):
    S = 0.0
    for i in range(len(q) - 1):
        v = (q[i + 1] - q[i]) / dt
        S += (0.5 * m * v * v - pot(0.5 * (q[i] + q[i + 1]), p)) * dt
    return S

def relax(q0, qT, pot, p, n=64, dt=0.02, m=1.0, iters=3000, lr=0.3):
    q = [q0 + (qT - q0) * i / (n - 1) for i in range(n)]
    for _ in range(iters):
        g = [0.0] * n
        for i in range(1, n - 1):
            g[i] = (m * (2 * q[i] - q[i - 1] - q[i + 1]) / dt
                    - 0.5 * dt * (_dV(pot, 0.5 * (q[i - 1] + q[i]), p)
                                  + _dV(pot, 0.5 * (q[i] + q[i + 1]), p)))
        for i in range(1, n - 1):
            q[i] -= lr * dt * g[i]
    resid = max(abs(gi) for gi in g[1:-1]) if n > 2 else 0.0
    return q, action(q, dt, pot, p, m), resid

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--q0", type=float, required=True)
    ap.add_argument("--q1", type=float, required=True)
    ap.add_argument("--potential", choices=sorted(POTENTIALS), required=True)
    ap.add_argument("--k", type=float, default=1.0)
    ap.add_argument("--g", type=float, default=9.8)
    ap.add_argument("--m", type=float, default=1.0)
    ap.add_argument("--n", type=int, default=64)
    ap.add_argument("--dt", type=float, default=0.02)
    a = ap.parse_args()
    pot = POTENTIALS[a.potential]
    p = {"k": a.k, "g": a.g, "m": a.m}
    q, S, resid = relax(a.q0, a.q1, pot, p, n=a.n, dt=a.dt, m=a.m)
    print(json.dumps({
        "model_type": "least-action",
        "potential": a.potential,
        "action": round(S, 8),
        "euler_lagrange_residual": resid,
        "computation_status": "passed" if resid < 1e-3 else "failed",
        "path": [round(x, 6) for x in q],
    }, indent=2))

if __name__ == "__main__":
    main()
