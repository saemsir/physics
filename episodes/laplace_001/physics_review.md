# Mathematical review: laplace_001

## Claim and model

- **Claim:** The unilateral Laplace transform turns the derivative in an
  initial-value problem into multiplication by `s` plus an explicit
  initial-value term. For the selected problem, the transformed equation is
  algebraic and can be inverted to recover the time-domain solution.
- **Definitions:** `X(s) = L{x}(s) = integral_0^infinity exp(-s tau) x(tau)
  d tau`; `s` is the transform variable. In the worked visualization, `tau`
  and `s` are dimensionless and `s` is taken real and positive for the
  integral illustration.
- **Assumptions:** `x` is piecewise continuously differentiable and of
  exponential order so the unilateral Laplace transform and integration by
  parts are valid in a right half-plane. The model is
  `dx/dtau + x = 1`, with `x(0+) = 0`.
- **Domain:** For this example the transforms converge for `Re(s) > 0`.
  More generally, transform existence and inversion require suitable
  regularity and a common region of convergence; the transform is not
  asserted to exist for every function or every `s`.
- **Source:** MIT OpenCourseWare, 18.03SC Differential Equations, Fall 2011,
  Unit III introduction:
  https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/pages/unit-iii-fourier-series-and-laplace-transform/
  Consulted 2026-10-17.

## Derivation

By integration by parts on a finite interval and then taking the limit where
the boundary term vanishes in the region of convergence:

`L{x'} = integral_0^infinity exp(-s tau) x'(tau) d tau`

`= [exp(-s tau)x(tau)]_0^infinity + s integral_0^infinity exp(-s tau)x(tau)d tau`

`= sX(s) - x(0+)`.

Also `L{1}=1/s` for `Re(s)>0`. Applying these rules to the initial-value
problem:

`sX(s) - 0 + X(s) = 1/s`

`X(s) = 1/[s(s+1)] = 1/s - 1/(s+1)`.

Inverting term by term gives `x(tau)=1-exp(-tau)` for `tau >= 0`.

## Verification

- **Initial condition:** `x(0+) = 1 - 1 = 0`.
- **Differential equation:** `x' = exp(-tau)`, so `x' + x =
  exp(-tau) + 1 - exp(-tau) = 1`.
- **Long-time behavior:** `lim_(tau->infinity) x(tau)=1`, consistent with
  the equilibrium of `x'+x=1`.
- **Transform check:** `L{1-exp(-tau)} = 1/s - 1/(s+1) =
  1/[s(s+1)]` for `Re(s)>0`.
- **Units:** Time and state in the illustrative equation are dimensionless.
  A dimensional physical model would require coefficients with consistent
  units and a correspondingly dimensioned transform variable.
- **Convention:** This is the unilateral transform, with the initial value
  at `0+` appearing explicitly. Do not silently substitute a bilateral
  transform convention.

## Mathematics gate

- [x] The derivative property is derived by integration by parts.
- [x] Initial condition and transform convention are explicit.
- [x] Convergence domain for this example is stated.
- [x] Recovered solution is checked in the original equation.
- [ ] Teacher has reviewed and approved the mathematics.

- **Status:** draft; approval required
- **Reviewer:**
- **Date:**
- **Open issues:** Confirm the course/source citation and preferred notation
  before recording.
