# Voice component license audit

Audit date: 2026-08-05

This is a source-grounded planning audit, not legal advice or a technical
benchmark. Engines and assets are evaluated separately; an engine's license does
not grant rights to its models, voices, or training data. `Accept` means the
reviewed combination can proceed to technical evaluation under Hecate's free
production-path policy. It does not select a default.

## Production policy

Production-default engines and bundled models or voices must be freely
redistributable and commercially usable without per-user fees. Required notices
must be shipped. Restricted, noncommercial, or ambiguous assets are research
only and cannot block a fully functional free path. Every selected artifact must
be pinned by version or digest in the maintained provenance manifest.

## Wake word and keyword spotting

| Candidate | Code | Model/data | Redistribution and commercial use | Notice, account, and cost | Result |
| --- | --- | --- | --- | --- | --- |
| openWakeWord engine | Apache-2.0 | Included pretrained models are CC BY-NC-SA 4.0 because training data include unknown or restrictive licenses | Code: permitted with Apache terms. Included models: noncommercial and therefore ineligible for defaults | Preserve Apache license/NOTICE; no runtime account or API key documented; no recurring engine fee | **Code accept; bundled models reject** |
| Custom openWakeWord `Hey Hecate` model | Apache-2.0 engine | Not yet created; training sources and generated audio licenses are undecided | Cannot approve redistribution or commercial use before every training input and resulting model license is recorded | No runtime key expected; training-source attribution and costs remain unresolved | **Needs review** |
| microWakeWord training/runtime family | Apache-2.0 | Available models are maintained separately; no audited `Hey Hecate` model was identified | Code is commercially usable; a default model is not approved until its model card and all training-source terms pass review | Preserve Apache notices; no runtime account or recurring fee identified | **Code accept; model needs review** |
| Picovoice Porcupine | GitHub wrapper is labeled Apache-2.0, but the operational SDK/service remains subject to Picovoice terms | Custom keyword is generated through Picovoice Console/API | Terms describe revocable, non-transferable, non-sublicensable access and possible fees; unsuitable for a freely redistributable default | Account and secret AccessKey required; free access is a limited trial and commercial terms may require payment | **Reject as production default** |

Primary evidence: [openWakeWord licensing](https://github.com/dscripka/openWakeWord#license),
[microWakeWord repository](https://github.com/OHF-Voice/micro-wake-word),
[Porcupine setup requirements](https://picovoice.ai/docs/quick-start/porcupine-python/),
and [Picovoice terms](https://picovoice.ai/docs/terms-of-use/).

## Local speech-to-text

| Candidate | Code | Model/data | Redistribution and commercial use | Notice, account, and cost | Result |
| --- | --- | --- | --- | --- | --- |
| whisper.cpp with official OpenAI Whisper weights | MIT | OpenAI states both Whisper code and model weights are MIT | Redistribution and commercial use permitted | Preserve MIT copyright/license notices; no account, API key, or recurring fee for local use | **Accept for benchmarking** |
| Vosk API with `vosk-model-small-en-us-0.15`, `vosk-model-en-us-0.22`, or `vosk-model-en-us-0.22-lgraph` | Apache-2.0 | Each named English model is explicitly listed as Apache-2.0 | Redistribution and commercial use permitted under Apache terms | Ship license and applicable notices; no account, API key, or recurring fee documented | **Accept for benchmarking** |

Primary evidence: [whisper.cpp license](https://github.com/ggml-org/whisper.cpp/blob/master/LICENSE),
[OpenAI Whisper code and weights statement](https://github.com/openai/whisper#license),
[Vosk API license](https://github.com/alphacep/vosk-api), and
[Vosk model-by-model licenses](https://alphacephei.com/vosk/models).

## Local text-to-speech and voices

| Candidate | Code | Model/voice/data | Redistribution and commercial use | Notice, account, and cost | Result |
| --- | --- | --- | --- | --- | --- |
| Kokoro inference library with Kokoro-82M | Apache-2.0 | Repository labels weights and voice files Apache-2.0 and publishes digests; training card identifies some CC BY sources but does not give a complete per-English-voice source/license mapping | Repository license permits both, but the incomplete per-voice provenance prevents production-default approval | Preserve Apache notices and cited CC BY attribution; no local account/key or recurring fee documented | **Needs provenance review** |
| Piper 1 GPL engine with `en_US-lessac-medium` | GPL-3.0 | Voice card links to the Lessac dataset license; the collection warns that individual voices can be restrictive | GPL permits commercial redistribution if its source/license duties are met; the voice remains unapproved until its linked dataset/voice terms are captured and reviewed | Provide GPL source/notice obligations and voice attribution; no local account/key or recurring fee documented | **Needs voice review** |
| Coqui TTS with XTTS-v2 | MPL-2.0 engine | XTTS-v2 is CPML and requires terms acceptance | Engine can be commercially used under MPL duties; XTTS-v2 cannot provide the required unrestricted commercial default | Preserve MPL notices/source duties; model requires terms acceptance and has no dependable free commercial license path | **Reject XTTS-v2 as production default** |

Primary evidence: [Kokoro code license](https://github.com/hexgrad/kokoro/blob/main/LICENSE),
[Kokoro model card](https://huggingface.co/hexgrad/Kokoro-82M),
[Kokoro voice inventory](https://huggingface.co/hexgrad/Kokoro-82M/blob/main/VOICES.md),
[Piper engine license](https://github.com/OHF-Voice/piper1-gpl),
[Piper voice-license guidance](https://github.com/OHF-Voice/piper1-gpl/blob/main/docs/VOICES.md),
[Lessac voice card](https://huggingface.co/rhasspy/piper-voices/blob/main/en/en_US/lessac/medium/MODEL_CARD),
[Coqui engine license](https://github.com/coqui-ai/TTS/blob/dev/LICENSE.txt), and
[Coqui model manifest](https://github.com/coqui-ai/TTS/blob/dev/TTS/.models.json).

## Speaker enrollment and identification

| Candidate | Code | Model/data | Redistribution and commercial use | Notice, account, and cost | Result |
| --- | --- | --- | --- | --- | --- |
| SpeechBrain with `spkrec-ecapa-voxceleb` | Apache-2.0 | Model card labels weights Apache-2.0; the model was trained on VoxCeleb, whose underlying recordings and downstream commercial-rights chain are not fully resolved by the model card | Code and stated weight license permit both, but training-data provenance ambiguity prevents production-default approval | Preserve Apache notices and model citation; no local account/key or recurring fee documented | **Needs legal/provenance review** |
| Resemblyzer bundled `pretrained.pt` | Apache-2.0 code | Weight is bundled, but the repository does not provide a separate model card with complete training-data/license provenance | Package redistribution appears intended, but model commercial-rights provenance is insufficient for the default policy | Preserve Apache notices; no local account/key or recurring fee documented | **Needs provenance review** |

Primary evidence: [SpeechBrain licensing](https://github.com/speechbrain/speechbrain#license),
[ECAPA model card](https://huggingface.co/speechbrain/spkrec-ecapa-voxceleb),
[VoxCeleb project](https://www.robots.ox.ac.uk/~vgg/data/voxceleb/),
[Resemblyzer repository](https://github.com/resemble-ai/Resemblyzer), and
[bundled-weight package declaration](https://github.com/resemble-ai/Resemblyzer/blob/master/setup.py).

Speaker identity remains a convenience signal only. Whatever component is
eventually selected must comply with the local consent, caregiver authorization,
immediate suspension, confirmed deletion, and no-sensitive-authorization rules
in the [Step Zero gates](STEP_ZERO_GATES.md).

## Current shortlist and exclusions

- **Production-eligible for technical benchmarking:** whisper.cpp with official
  Whisper weights; Vosk API with only the three explicitly listed Apache-2.0
  English models above.
- **Engine-only candidates:** openWakeWord and microWakeWord, pending a fully
  attributable, commercially usable `Hey Hecate` model.
- **TTS needs review:** Kokoro-82M and Piper with Lessac may be benchmarked only
  after the unresolved per-voice provenance/terms are closed. There is no
  production-approved TTS voice from this audit yet.
- **Speaker ID needs review:** SpeechBrain ECAPA and Resemblyzer need a clearer
  model/data rights chain before becoming defaults.
- **Excluded from production defaults:** openWakeWord's bundled noncommercial
  models, Picovoice Porcupine, and Coqui XTTS-v2.

The next license step is documentary, not a download: pin candidate revisions,
capture complete notices, resolve the `Hey Hecate` training-data plan, and close
the TTS and speaker-model provenance gaps before technical benchmarking.
