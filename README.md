# Momentrix

> **Turn Hours into Moments.**
> AI-powered viral short video creator. Free, private, and open source: run it on your own computer or server with your own AI key.

Paste a YouTube, Twitch or Kick link (or upload any video file) and **Momentrix** automatically discovers the most viral moments, crops them to 9:16 Shorts/Reels/TikTok format, adds word-by-word animated captions, and generates engaging hooks and viral titles.

---

## ⚡ What Makes Momentrix Special

- **100% Free & Self-Hosted:** No subscription fees, paywalls, or hidden costs. You own your data, videos, and outputs.
- **Bring Your Own Key (BYOK):** Use free-tier keys like Google Gemini (generous free daily quota) or Groq, or run completely offline with local models using Ollama.
- **English & Hinglish Captions:** Built-in romanization engine (`studio/roman.py`) and prompt calibration (`studio/brain.py`) transcribe and caption both English and Hindi/Urdu speech cleanly in Latin letters (Hinglish: *"yaar ye kya hai"*), styled for TikTok, Reels, and YouTube Shorts fonts.
- **Local Speech Recognition:** Transcribes speech locally on your CPU or GPU using the Parakeet 0.6b model via `sherpa-onnx`. Audio never leaves your computer.
- **5 Viral Caption Presets:**
  - `bounce`: Energetic kinetic punch with primary highlight colors.
  - `hype`: High-intensity viral framing.
  - `clean`: Minimalist modern aesthetic.
  - `hormozi`: High-contrast yellow/green punch words on bold black background.
  - `neon`: Electric violet & cyan glow.
- **4 Dynamic Video Layouts:** Blur background, Smart Zoom, Smart Crop, and Split Gaming/Reaction layout.
- **Cyber Shield & Protection:** Built-in server gatekeeper intercepting path traversal, XSS, and SQL injection, coupled with frontend route verification (`#guarddlg`) that intercepts unauthorized URL tampering in real time.
- **Zero Login Friction:** Single-user direct root access by default. Opens directly to the studio without sign-up friction. (Multi-user accounts can be activated anytime with `MOMENTRIX_ACCOUNTS=1`).

---

## 🚀 Quick Start

### Prerequisites
- **Python 3.10+**
- **FFmpeg**:
  - Windows: `winget install Gyan.FFmpeg`
  - macOS: `brew install ffmpeg`
  - Linux: `sudo apt install ffmpeg`

### 1. Installation
Clone the repository into a permanent folder (e.g., `E:\Momentrix Clip` or `C:\momentrix`):

```bash
git clone <repository-url> "C:\momentrix"
cd "C:\momentrix"
pip install -r requirements.txt
```

### 2. Launch Momentrix

**On Windows:**
Double-click `run.bat` or run:
```bash
python -m studio.server
```

*(On first start, the speech model downloads automatically: ~480 MB, one-time only).*

Open your browser at:
👉 **`http://127.0.0.1:8765`** (Opens the Momentrix Landing Page; click **Get started** to enter the Studio at `/app`).

---

## 🔑 AI Providers (Free & BYOK)

Momentrix connects to your preferred AI model to identify viral moments, generate hooks, and format captions:

| Provider | Service | Free Tier / Getting an API Key | Example Model |
|---|---|---|---|
| `gemini` | **Google Gemini (Recommended)** | [Google AI Studio (Free)](https://aistudio.google.com/apikey) | `gemini-2.5-flash` |
| `groq` | **Groq Cloud** | [Groq Console (Fast & Free Tier)](https://console.groq.com/keys) | `llama-3.3-70b-versatile` |
| `ollama` | **Ollama (100% Offline)** | [Ollama.com (No Key Required)](https://ollama.com) | `llama3.1` |
| `openai` | **OpenAI** | [OpenAI Platform](https://platform.openai.com/api-keys) | `gpt-4o-mini` |
| `xai` | **Grok (xAI)** | [xAI Console](https://console.x.ai) | `grok-4` |
| `openrouter` | **OpenRouter** | [OpenRouter Keys](https://openrouter.ai/keys) | `google/gemini-2.5-flash` |
| `anthropic` | **Claude** | [Anthropic Console](https://console.anthropic.com) | `claude-3-5-haiku-latest` |
| `custom` | **Custom Endpoint** | Any OpenAI-compatible local/remote host | Specify in Settings |

You can configure your provider directly from the dashboard (**Settings → AI**) or in `.env`:
```ini
MOMENTRIX_AI_PROVIDER=gemini
MOMENTRIX_AI_MODELS=gemini-2.5-flash
MOMENTRIX_AI_KEY=your_gemini_key_here
```

---

## 🛡️ Cyber Shield & Security

Momentrix includes a hardened multi-layer security architecture:
1. **Server Gatekeeper (`studio/server.py`)**:
   - Blocks path traversal attacks (`..`, `%2e%2e`, `../../`).
   - Blocks script injection (`<script>`, `javascript:`) and SQL injection (`UNION SELECT`).
   - Enforces strict security headers: `X-Content-Type-Options: nosniff`, `X-Frame-Options: DENY`, `X-XSS-Protection: 1; mode=block`, `Content-Security-Policy`, and Cache-Busting on dynamic endpoints.
2. **Client-Side Cyber Guard (`web/index.html`)**:
   - Continuous route verification on `hashchange` and `popstate`.
   - If an unauthorized path or URL tampering is detected, a centered **Cyber Guard Notice Modal** appears on the screen with security details and a safe one-click recovery back to the studio.

---

## 🧪 Testing & Verification

Run the comprehensive 56-assertion test suite:
```bash
python tests/test_momentrix_suite.py
```

Run rendered DOM element-by-element verification:
```bash
python tests/verify_dom.py
```

---

## 📁 Project Structure

```
├── studio/               # FastAPI backend & pipeline engine
│   ├── server.py         # Web routes, gatekeeper security, and headers
│   ├── ai.py             # Multi-provider AI interface (Gemini, Groq, OpenAI, etc.)
│   ├── brain.py          # Viral clip scouting, hooks, and prompt engineering
│   ├── roman.py          # English & Hinglish phonetic caption romanization
│   ├── render.py         # Video cropping, 9:16 layout, and subtitle burns
│   ├── transcribe.py     # Local Sherpa-ONNX speech-to-text pipeline
│   └── jobs.py           # Background processing queues
├── web/                  # Studio frontend (Modern Dark Tech UI)
│   ├── index.html        # Main SPA interface with Cyber Guard dialog
│   └── landing.html      # Momentrix landing page
├── tests/                # Automated security and DOM test suites
├── run.bat               # One-click Windows launch script
└── requirements.txt      # Python dependencies
```

---

## 📄 License

Distributed under the [MIT License](LICENSE). Caption typography in `studio/fonts/` (Anton, Archivo Black, Poppins) is licensed under the SIL Open Font License.
