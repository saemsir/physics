# Visual teaching principles

SaemPhysics visuals serve the physics, not a trend or borrowed creator style.
Use visualizations to make a mathematical or physical relationship easier to
inspect, reason about, and check. Academic accuracy, explicit assumptions, and
clear derivations take priority over novelty or pace.

## Research standard

Build lessons from:

- Richard Feynman's lectures and books for conceptual reasoning and physical
  intuition.
- MIT-level professor lectures and course materials for rigorous explanations
  and derivations.
- Established textbooks and other scholarly books for definitions, models,
  derivations, and independent checks.
- 3Blue1Brown as a reference for mathematical visualization and explanatory
  sequencing, while independently verifying every mathematical claim against
  trusted course materials or books.

Record the exact source, author or lecturer, edition or course, section or
timestamp, stable URL when available, and date consulted. A respected source
still needs context: verify definitions, assumptions, signs, units, limiting
cases, and derivations. Resolve disagreements explicitly and keep teacher
approval as a required gate.

## Turn reasoning into visuals

1. Define the quantity, model, coordinate convention, and assumptions before
   animating them.
2. Choose a diagram that faithfully represents the model. Mark schematic
   diagrams as schematic; do not imply scale unless the construction preserves
   it.
3. Animate only meaningful changes: motion, geometry, color, or labels should
   correspond to a quantity, operation, or inference in the explanation.
4. Keep symbols, units, directions, and color meanings consistent. Never make
   color the only way to distinguish quantities.
5. Show enough intermediate reasoning that a learner can follow and check the
   conclusion. Do not trade a necessary step for a faster reveal.
6. Review the rendered scene at normal speed and phone size; fix collisions,
   illegible labels, misleading motion, and unsupported visual implications.

## Representation-bridge lessons

When a concept becomes clearer in a different representation, make the
mathematical bridge—not a visual metaphor—the center of the explanation:

1. Show the original problem and identify the operation that makes it hard.
2. Define the new representation and explain how it is constructed.
3. Derive how the relevant operation changes under that representation;
   expose important boundary or initial-condition terms.
4. Solve one tractable example in the new representation.
5. Map back to the original representation and independently verify the
   result there.
6. State the transform's assumptions and domain of validity. Avoid suggesting
   it is merely a relabeling, a magic trick, or a frequency plot when it is not.

[`../templates/representation_bridge.md`](../templates/representation_bridge.md)
provides a reusable storyboard structure. The Laplace pilot in
[`../episodes/laplace_001/storyboard.md`](../episodes/laplace_001/storyboard.md)
demonstrates the pattern with an original, dimensionless first-order ODE.

## Review before approval

- [ ] Each claim is supported by a traceable, appropriate academic source.
- [ ] The model, assumptions, axes, signs, units, and domain are explicit.
- [ ] The derivation and result have an independent physics or mathematics
  check.
- [ ] Every visual change corresponds to the reasoning and preserves the
  intended meaning.
- [ ] If a representation changes, the forward map, transformed operation,
  inverse map, and validity conditions are made explicit.
- [ ] Labels remain legible and the explanation does not rely on color alone.
- [ ] The learner can inspect the reasoning rather than only see the answer.
- [ ] A teacher has reviewed the physics and the rendered preview.

Use original scripts, examples, diagrams, and visual identity. Learn from
sound reasoning and visualization principles; do not reproduce protected
wording, artwork, or distinctive scenes.
