# Deploying Momentrix to a Server

Momentrix runs efficiently in Docker containers on any Linux server: the app, PostgreSQL, and Caddy (automatic HTTPS reverse proxy).

---

## Hardware Requirements

- **Linux Server with Docker** (Ubuntu 22.04 / 24.04 recommended).
- **Compute**: Clipping and transcription are CPU/GPU-driven: plan on **4–8+ CPU cores, 8–16 GB RAM, and 100+ GB disk**.
- **Domain**: An `A` record pointing to your server's public IP.
- **AI Key**: A free Google Gemini or Groq key (configured via `Settings → AI`).

---

## Quick Deployment Steps

1. Clone your repository to the server:
   ```bash
   git clone https://github.com/basavarajrevani/MomentrixClip.git /opt/momentrix
   cd /opt/momentrix
   ```

2. Configure environment:
   ```bash
   cp .env.example .env
   ```
   Set your domain and settings in `.env`:
   ```ini
   MOMENTRIX_DOMAIN=your-domain.com
   MOMENTRIX_PUBLIC_URL=https://your-domain.com
   COMPOSE_PROFILES=own-https
   ```

3. Launch with Docker Compose:
   ```bash
   docker compose up -d --build
   ```
   *The speech-to-text model (~480 MB) downloads automatically on first launch.*

4. Access your studio:
   Open `https://your-domain.com/app` directly in your browser.

5. (Optional) For multi-user servers, enable sign-in (`MOMENTRIX_ACCOUNTS=1`), sign up, and grant admin rights:
   ```bash
   docker compose exec app python -m studio.admin grant your-email@domain.com
   ```

---

## Social Platform Auto-Posting (Optional)

Creators can connect their YouTube, Instagram, and TikTok accounts directly in **Settings → Connected apps** for seamless 1-click scheduling or automated posting.

- **YouTube**: Google Cloud OAuth 2.0 Web Client with YouTube Data API v3 enabled.
- **Instagram**: Meta Developer Business App with Instagram Content Publishing API.
- **TikTok**: TikTok Developer App with Content Posting API.
