# Working on Momentrix

Architecture and contributor guide for Momentrix AI Viral Clip Studio.

---

## Brand & Workspace Configuration

Momentrix runs locally at `http://127.0.0.1:8765/app`. Keep folder paths short on Windows (`E:\Momentrix Clip` or `C:\momentrix`) to prevent path length limitations when loading speech-to-text models.

---

## Running & Testing

- **Run Server**: `python -m studio.server` (or double click `run.bat`).
- **Pre-download Speech Model**: `python -m studio.fetch_model`.
- **Run Security & API Test Suite**: `python tests/test_momentrix_suite.py`.
- **Run Rendered DOM Verification**: `python tests/verify_dom.py`.

---

## Directory Overview

| File / Folder | Role |
|---|---|
| `studio/server.py` | FastAPI route endpoints, gatekeeper cyber defense, and security headers |
| `studio/config.py` | Configuration settings parsed from environment variables |
| `studio/ai.py` | Multi-provider AI interface (Gemini, Groq, Ollama, OpenAI, Anthropic, OpenRouter) |
| `studio/brain.py` | Clip scouting, hook generation, viral titles, and prompt tuning |
| `studio/roman.py` | English and Hinglish Roman caption engine |
| `studio/jobs.py` | Video processing queue and worker execution |
| `studio/live.py` | Live stream capture, chat spike detection, and realtime highlight extraction |
| `studio/transcribe.py` | Local speech-to-text transcription engine (Sherpa-ONNX / Parakeet) |
| `studio/render.py` | 9:16 layout composition, kinetic subtitles, and video rendering (FFmpeg) |
| `studio/media.py` | Media ingestion (`yt-dlp`), audio normalization, and stream probing |
| `studio/db.py` | Database abstraction layer (SQLite / PostgreSQL) |
| `web/index.html` | Momentrix Studio single-page app (no build step, pure dark obsidian glass tech theme) |
| `web/landing.html` | Momentrix marketing landing page |

---

## Engineering Standards

- **Single-User Root Access**: Enabled by default (`MOMENTRIX_ACCOUNTS=0`). Opens straight into workspace without login friction.
- **Client Session Context**: Request origin is tracked via session tokens (`ctx.uid()`), never client parameters.
- **Untrusted Media Data**: Transcripts and metadata from external videos are sanitized through `brain._safe`.
- **Cyber Shield Gatekeeper**: Unauthorized traversal attempts, injection payloads, or tampering prompt the `#guarddlg` modal alert.
