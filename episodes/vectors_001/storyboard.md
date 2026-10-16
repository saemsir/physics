# Storyboard: vectors_001

**Scene ID:** `vector_components`
**Target duration:** 30-60 seconds
**Screen convention:** schematic Cartesian grid; positive x right, positive y
up. Diagram coordinates are not physical units.

| Beat | Visual action | Narration cue | Learner should notice |
|---|---|---|---|
| Hook | Show a diagonal vector from the origin to `(3, 2)`. | "How can we describe this diagonal arrow using simpler moves?" | One endpoint can be reached by multiple directed steps. |
| Horizontal component | Draw from `(0, 0)` to `(3, 0)`. | "First move three units in the positive x direction. That is the x-component." | `A_x = 3` and points right. |
| Vertical component | Continue from `(3, 0)` to `(3, 2)`. | "Then move two units in the positive y direction. That is the y-component." | `A_y = 2` and points up. |
| Rebuild | Keep the component arrows and diagonal visible together. | "Put the two moves tip-to-tail and you arrive at the original endpoint." | The component vectors sum to the diagonal vector. |
| Equation and recap | Reveal the unit-vector expression and magnitude check. | "So A is three i-hat plus two j-hat. Add vectors by direction, not by adding their lengths as ordinary numbers." | `A = 3 i-hat + 2 j-hat`; `|A| = sqrt(13)`, not `5`. |

## Design gate

- **Status:** draft; teacher approval required
- **Reviewer:**
- **Date:**
- **Visual risk:** Keep the equation clear of the number plane and labels.
- **Production note:** Add narration in post-production after the preview timing
  is reviewed; the Manim scene does not generate voice audio.
