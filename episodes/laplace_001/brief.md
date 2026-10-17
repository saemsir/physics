# Episode brief: laplace_001

- **Working title:** When a differential equation becomes algebra
- **Primary audience:** Learners meeting first-order linear differential
  equations and the unilateral Laplace transform
- **Language:** English
- **Target duration:** 2-3 minutes
- **Central question:** How can changing the representation turn a
  differential equation into an algebra problem without losing its initial
  condition?
- **Learning outcome:** Explain the derivative rule for the unilateral
  Laplace transform, use it to solve one initial-value problem, and verify
  the recovered solution in the original equation.
- **Prerequisites:** Differentiation, integration by parts, partial fractions,
  and the idea of an initial-value problem
- **Likely misconception:** The transform is only a relabeling or a graph of
  frequency; the initial condition can be ignored; an algebraic answer in
  `s` is already the time-domain solution.
- **Scope and non-goals:** Use a dimensionless, first-order, constant
  coefficient example. Do not attempt to explain the full complex-plane
  interpretation, transfer functions, convolution, impulses, or numerical
  inversion in this episode.
- **Key claims or equations:** `L{x'} = sX(s) - x(0+)`;
  `x' + x = 1`, `x(0)=0` gives `X(s)=1/[s(s+1)]` and
  `x(t)=1-e^(-t)`, for the stated convergence domain.
- **Planned scenes:** The original initial-value problem; the weighted
  integral representation; integration by parts and the initial-value term;
  algebraic solution and inverse transform; verification in the original
  equation.
- **Practice / exam connection:** Identify the transformed derivative and
  initial-value term in a related first-order equation.
- **Success criteria:** Learners can explain what became easier, where the
  initial condition went, and check the result by substitution.

## Source and originality note

The MIT OpenCourseWare 18.03SC Unit III introduction states that the Laplace
transform represents a function in a different independent variable, converts
a differential equation for `x(t)` into an algebraic equation for `X(s)`, and
allows recovery of `x(t)` after solving. The example and wording in this
episode are original and do not reproduce another creator's script or scenes.

The linked 3Blue1Brown video is recorded as a visualization reference only.
Its public metadata identifies the title as *Why Laplace transforms are so
useful* ([video](https://youtu.be/FE-hM1kRK4Y), metadata checked 2026-10-17),
but playback and captions were unavailable during preparation; no claim is
made here about its complete sequence or details.

## Editorial gate

- **Status:** draft; teacher approval required
- **Reviewer:**
- **Date:**
- **Notes:** This is a storyboard/derivation pilot, not an approved or rendered
  lesson.
