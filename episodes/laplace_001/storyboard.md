# Storyboard: laplace_001

**Scene ID:** `laplace_representation_bridge`
**Target duration:** 2-3 minutes
**Status:** original draft; mathematics, narration, and preview require teacher
approval.
**Screen convention:** dimensionless time `tau`; for the visual integral,
real `s > 0`. The full transform variable may be complex, with a stated
region of convergence.
**Source:** MIT OpenCourseWare 18.03SC Unit III introduction and the
independently checked derivation in `physics_review.md`.

| Beat | Visual action | Narration cue | Learner should notice |
|---|---|---|---|
| Question | Put `x' + x = 1`, `x(0)=0` on screen. Emphasize the derivative and the initial value separately. | "A derivative equation is hard to solve directly. Can we change representations so the calculus becomes algebra—and still keep the starting value?" | The task is an initial-value problem, not just an equation to manipulate. |
| Define the new view | Show `X(s) = integral_0^infinity e^(-s tau) x(tau) d tau`. With a fixed positive `s`, show the weight `e^(-s tau)` over time and the weighted accumulation. Keep the curve and integral visible together. | "The Laplace transform assigns a weighted integral to the whole time signal. Changing `s` changes the weighting and gives a new function `X(s)`." | `X(s)` is a new representation of the signal, defined by an integral; it is not simply the original graph relabeled as frequency. |
| Transform the derivative | Reveal integration by parts in two deliberate steps. Show the endpoint contribution at `tau=0` separately, then identify `sX(s) - x(0+)`. | "Integration by parts turns the derivative into multiplication by `s`, but it also leaves a boundary term: the initial value." | The initial condition is carried into the transformed equation, not discarded. |
| Solve the algebra | Apply the transform to the model: `sX(s) - 0 + X(s) = 1/s`. Rearrange to `X(s)=1/[s(s+1)]`, then show partial fractions. | "Now the differential equation is an algebraic equation in `X`. Solve it, then split it into familiar transform pairs." | The operation has changed in a useful, derived way. |
| Return to time | Map `1/s - 1/(s+1)` back to `1 - e^(-tau)`. Keep the source expression and recovered expression connected. | "The inverse transform returns the answer to the original time variable." | An `s`-domain result is an intermediate answer; the lesson's output is still `x(tau)`. |
| Verify and qualify | Substitute `x=1-e^(-tau)` and its derivative into the original ODE. Show `x(0)=0`, `x'+x=1`, and a brief note: unilateral transform, regularity/exponential-order assumptions, `Re(s)>0` here. | "Check it where the question began: the initial value is right, and the equation balances. The transform is powerful, but it has assumptions and a convergence domain." | The representation bridge is reversible for this example and the result is independently checkable. |

## Visual risks

- Do not depict the transform as merely a Fourier/frequency spectrum; `s` is
  generally complex and the integral definition is the key idea here.
- Do not hide the integration-by-parts boundary term or initial value.
- Do not suggest the transform exists for every function or every value of
  `s`; state the region of convergence and assumptions concisely.
- Keep the time signal, weighted integral, algebraic equation, and recovered
  time signal visually distinct while making their relationship explicit.
- Avoid decorative motion. The weighting, algebra, and inverse mapping are
  the only transformations that need to move.

## Design gate

- **Reviewer:**
- **Date:**
- **Visual risks:** Prevent symbolic equations from crowding the integral and
  its changing weight; use a separate, readable region for derivation.
- **Production note:** Develop and review the physics, script, and storyboard
  before writing a Manim scene. Render only after the derivation and scene
  transitions are approved.
