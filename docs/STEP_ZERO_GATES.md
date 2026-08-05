# Step Zero exit gates

Step Zero turns product direction into testable local contracts. A numbered
step must not be marked complete, and work must not be promoted beyond it, until
its repository issue has every acceptance item checked and public-safe evidence
has been reviewed.

GitHub stores planning and aggregate results only. Raw audio, transcripts,
biometric artifacts, household details, device identifiers, credentials,
private logs, usernames, hostnames, serial numbers, and resolved local paths
remain local and uncommitted.

## Step 0.2: voice-stack validation

The voice-stack gate requires reproducible evidence for:

- licenses and sources for every evaluated engine, runtime, model, and weight;
- a complete offline voice loop with network access disabled;
- consented, local child/adult wake-phrase and false-activation testing;
- local English transcription of Hecate and core vocabulary;
- natural, responsive local TTS on the CPU fallback path;
- local neutral-phrase speaker enrollment and complete deletion;
- an explicit ban on speaker identity as sensitive-action authorization;
- pre-rendered common phrases instead of training a voice model; and
- aggregate accuracy, latency, memory, CPU/GPU, and false-activation results.

## Step 0.3: hardware and power validation

The hardware and power gate requires reproducible evidence for:

- WSL2 visibility of the NVIDIA GPU through the Windows driver and selected
  CUDA runtime;
- reliable default microphone capture and speaker playback;
- responsive CPU wake and audio processing during representative GPU load;
- measured temperature and resource ceilings for sustained plugged-in use;
- controlled low-memory and low-storage degradation with clear status;
- compact starter and recommended storage tiers for the selected voice stack;
- battery transition behavior that stops wake listening, unloads heavy models,
  and never enables silent cloud fallback;
- health checks before resuming after AC power returns;
- a documented future local, always-on, UPS-backed Linux/headless server role;
  and
- NPU use remaining an optional future accelerator, not a first-release
  dependency.

Temperature and resource limits must come from applicable hardware guidance and
measured behavior; this policy does not invent universal thresholds. The gate
report records sanitized hardware classes, pass/fail results, latency, dropouts,
resource use, degradation behavior, and unresolved limitations.

Any unresolved safety, offline, audio-reliability, data-integrity, or
power-transition failure keeps the relevant gate open. Non-gating improvements
may move to follow-up issues only after that distinction is reviewed.
