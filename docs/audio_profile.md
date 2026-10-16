# Saem Physics narration profile

## Status and intent

The current profile lives in `config/audio_profile.json`. It defines an
original, clear educational narration direction for ages 14–21: warm, curious,
precise, and unhurried enough for equations. It takes broad production goals
from cinematic visual education, but it does not copy any particular
creator's distinctive voice, music, scripts, or sound design.

The sample has now been analyzed locally. It is a 65-second, 48 kHz,
16-bit stereo PCM WAV. Channel peaks are -1.82/-1.80 dBFS, RMS is -17.71 dBFS
per channel, DC offset is about 0.000032, there are no clipped samples, and
the level-based leading/trailing silence is 0.046/0 seconds. The signal
measurements are recorded in `config/audio_profile.json`.

The peak is close to digital full scale. There is no clipping, but lower the
input gain approximately 4–6 dB for future takes to retain recording
headroom. Do not alter the original sample just to hit that recording target.
The EQ ranges remain provisional because no auditory judgment of room noise,
plosives, sibilance, reverberation, or intelligibility has been made.

## Spoken mathematics and number pronunciation

The canonical, machine-readable rules are in
[`config/audio_profile.json`](../config/audio_profile.json), under
`spoken_math`. They are a script-writing and recording standard for English
educational narration, not an automatic text-to-speech system. Use clear,
internationally understandable English and SI unit names. Keep the speaker's
natural accent; consistency and correct mathematical meaning matter more
than imitating a particular accent.

The original first-batch scripts are in
[`episodes/batch_001/narration.json`](../episodes/batch_001/narration.json).
Each episode has separate vertical and horizontal lines keyed to the matching
storyboard beats and their fixed time windows. These are drafts for review,
not approved recordings or physics sign-off. The Colab notebook displays the
first episode's timed cues alongside each silent preview to let you rehearse
and check fit. It does not record or mix the voice.

### Script every equation before recording

Write the spoken line next to the displayed equation. Define each variable
the first time it appears, keep its spoken name consistent, and read all
signs, grouping, exponents, units, and precision. Never silently repair or
round a value in the spoken track. Pause between mathematical phrases, not
inside a number or unit.

| Written form | Say |
| --- | --- |
| `0.04` | “zero point zero four” |
| `3.050` | “three point zero five zero” (preserve the written precision) |
| `-2.5` | “negative two point five” |
| `a - b` | “a minus b” or “subtract b from a”, as the sentence requires |
| `(a + b) / c` | “the quantity a plus b, all divided by c” |
| `x^2`, `x^3`, `x^n` | “x squared”, “x cubed”, “x to the power of n” |
| `sqrt(x)` | “the square root of x” |
| `sin^-1(x)` | “inverse sine of x” or “arcsine of x”; not “sine to the minus one” |
| `(sin x)^2` vs `sin(x^2)` | “sine squared of x” vs “sine of x squared” |
| `log_b(x)` | “logarithm base b of x” |
| `dy/dx` | “dee y by dee x”; then explain it as the derivative of y with respect to x |
| `integral_a^b f(x) dx` | “the integral from a to b of f of x, with respect to x” |
| `6.02 x 10^23` | “six point zero two times ten to the power of twenty-three” |
| `m/s^2` | “metres per second squared” |

For numbers, say “zero,” never “oh” for the digit 0. Read decimal digits
individually when precision matters and preserve trailing zeros. Use
“negative” for a signed value and “subtract” for an operation. Read a
scientific-notation exponent explicitly, including “negative” where present.
Say “approximately” for rounded results. Use familiar names such as “one
half” only when they cannot hide the grouping; otherwise say “one over two”
or “the quantity … divided by …”.

### Functions, symbols, and units

- Say **sine**, **cosine**, and **tangent** (or “sine of theta”), not letter
  names. For inverse trig functions say **inverse sine** / **arcsine**,
  **inverse cosine** / **arccosine**, or **inverse tangent** / **arctangent**.
  Reserve “one over sine” or “cosecant” for the reciprocal.
- Say **natural log** for `ln`. For `log`, say the base if it is shown or
  relevant; do not assume every audience uses the same convention.
- Name Greek letters on first use: alpha, beta, gamma, delta, epsilon,
  theta, lambda, mu, nu, pi, rho, sigma, phi, psi, omega. The profile lists a
  consistent approximate English pronunciation for each. These spellings
  guide performance; do not pronounce the capital/lowercase glyph difference
  unless it matters.
- Say unit names fully in explanations: metres, seconds, metres per second,
  metres per second squared, kilograms, newtons, joules. Keep the value-unit
  pairing together; for example, “ten metres per second squared.”
- Say subscripts as “sub”: `v_0` is “v sub zero,” and `a_x` is “a sub x.”
  Say vector labels explicitly (“vector v”); explain components and order
  before reading a tuple or matrix.
- Say “change in x” for `Delta x` when explaining meaning; say “delta x”
  when reading the symbol itself. State whether angles are in degrees or
  radians.

### Mandatory ambiguity check

Before recording and caption approval, check negative values versus
subtraction; negative exponents; inverse versus reciprocal functions;
parentheses and fraction scope; squared function values versus squared
inputs; zero versus the letter O; exact equality versus approximation; unit
exponents; vector component order; and every numerical digit/unit against
the approved solution. A pronunciation guide or TTS engine cannot verify
the mathematics. Have a reviewer compare the spoken take and captions to the
approved equation and result.

## Voice sample handling

Voice recordings are personal data. The sample was uploaded to the repository
as `saem_voice_sample.wav`, so it is currently a tracked repository file and
will be present in GitHub checkouts. The Git ignore rule only prevents future
untracked copies; it does not untrack this existing file. The workflow does
not analyze or otherwise use the audio, and the analyzer emits only technical
measurements to the terminal without copying or modifying the WAV.

If this repository is public, the uploaded sample is accessible to repository
visitors. If the sample was meant to remain private, ask to remove it from the
tracked project; a normal deletion commit will not erase prior Git history.
Do not send it to an external audio service.

To repeat the read-only analysis on the local sample, run:

```bash
python tools/analyze_voice_sample.py /path/to/saem_voice_sample.wav
```

Use the output to set recording gain and decide whether cleanup is needed.
Listen privately to the sample for room tone, mouth clicks, plosives,
sibilance, reverberation, and microphone position before changing EQ.
Technical metadata alone cannot identify an ideal EQ curve or judge vocal
performance.

## Suggested recording and processing

1. Record in a quiet, soft-furnished room, mono PCM WAV at 48 kHz and 24-bit
   when practical. Keep microphone distance around 12–18 cm and slightly
   off-axis. Aim for peaks between -12 and -6 dBFS with no clipped samples.
2. Edit mistakes and handling noise with room-tone crossfades. Improve the
   room or mic position before denoising.
3. Try a 60–100 Hz high-pass filter only as needed. Use gentle noise reduction
   (about 3–6 dB) only when the unprocessed noise is actually distracting.
4. Make small EQ changes by ear. A broad 1–2 dB cut around 180–350 Hz may help
   muddiness; a broad 1–2 dB lift around 2–4 kHz may help intelligibility.
   These are optional ranges, not automatic boosts/cuts.
5. De-ess only harsh sibilants. Use gentle compression around 2:1–2.5:1 with
   roughly 2–4 dB gain reduction on stronger phrases. Automate phrase levels
   before makeup gain; use a true-peak limiter at -1 dBTP for the final mix.
6. Start narration around -16 LUFS integrated for a stereo web-video program,
   then verify the platform specification and listen on headphones, speakers,
   phone speakers, and in mono. Keep music low enough that every consonant and
   physics term stays intelligible.

For 60-second clips, a starting delivery pace of 125–150 words/minute gives
roughly 110–145 spoken words after allowing for pauses and visual beats. For
three-minute lessons, use roughly 115–140 words/minute and leave deliberate
space for calculations. Do not time-compress dense derivations just to fit.
Read a representative equation aloud during rehearsal; if the correct,
unhurried explanation does not fit, simplify the teaching scope rather than
speeding up or dropping mathematical detail.

## Workflow validation

`.github/workflows/validate-content-network.yml` runs tests, compiles the
content engine, checks the original solver-to-lesson flow, builds the first
batch manifest, and validates its 20 render briefs. It does not read the voice
sample or render videos. Audio processing remains a private, local/Colab
post-production stage.
