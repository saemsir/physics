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

## Workflow validation

`.github/workflows/validate-content-network.yml` runs tests, compiles the
content engine, checks the original solver-to-lesson flow, builds the first
batch manifest, and validates its 20 render briefs. It does not read the voice
sample or render videos. Audio processing remains a private, local/Colab
post-production stage.
