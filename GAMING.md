# Momentrix Gaming Mode

Momentrix includes a dedicated **Gaming & Reaction Mode** designed specifically for game streams and reaction videos. A gaming stream is mostly not just talk — it is gameplay, a facecam, and high-energy gamer reactions.

Momentrix incorporates three specialized engines to turn gaming streams into viral TikToks, YouTube Shorts, and Instagram Reels.

---

## 1. Automated Game Identification & Dynamic Tags

`studio/games.py` automatically detects the game being played from:
- The stream or video title
- Channel metadata or the creator's workspace settings

**23+ popular competitive and trending titles are supported out-of-the-box**, including *GTA VI, GTA V, Fortnite, Minecraft, Valorant, Elden Ring, Palworld, Helldivers 2, Cyberpunk 2077, Marvel Rivals, The Finals, Rocket League*, and more.

When a game is recognized:
- **AI Prompt Tuning (`studio/brain.py`)**: The AI is instructed to identify moments unique to that game: clutch plays, fails, jump scares, glitches, bosses, or extreme streamer reactions.
- **Smart Game Hashtags**: Clips automatically receive trending game tags (e.g., `#GTA6`, `#ViceCity`, `#RockstarGames` or `#ValorantClutch`, `#FortniteClips`), ensuring maximum reach in algorithmic feeds.

---

## 2. Crowd Reaction & Chat Spike Intelligence

In live Twitch or Kick streams, message volume alone can be misleading (e.g., emote spam or bot raids).

Momentrix tracks **distinct participants** rather than raw message volume (`studio/live.py`):
- **Participant-Weighted Spikes**: Chat activity is only classified as a genuine viral reaction spike when multiple unique viewers react simultaneously.
- **Signal Fusion**: Momentrix correlates chat participant spikes with audio loudness jumps (shouting, laughing, hype) and transcript sentiment to find true viral highlights.

---

## 3. Intelligent Facecam Detection & Split Gameplay Layout

Traditional 16:9 gaming streams letterboxed with blur leave the gameplay as a tiny strip in the middle. 

Momentrix's **Gameplay Layout** (`studio/render.py` & `studio/facecam.py`):
1. Fills the 9:16 vertical frame with the gameplay centered.
2. Automatically detects the streamer's webcam box using edge-variance stability algorithms and AI bounding-box confirmation.
3. Overlays the streamer's facecam at the top of the vertical short, so viewers see the gameplay action and the streamer's reaction simultaneously.

---

## 4. Ad-Break and AFK Filtering

`studio/quality.py` detects static screens, pause menus, and commercial breaks by tracking frame-to-frame pixel variance, ensuring that no ad breaks or AFK screens are clipped.

---

## Recommended Studio Settings for Gaming Streams

In **Momentrix Studio Options**:
- **Subtitle Style**: `hype` or `bounce`
- **Layout**: `gameplay` (or `zoom`)
- **Min Length**: `15s`
- **Max Length**: `60s`
- **Max Clips**: `6`
- **Quality**: `1080p Ultra`
