# 🎙️ Streamer-Agent

AI-powered side-kick for live-streamers.  
The agent (“**Tony**”) listens to chat, answers in real-time with a fun, sarcastic personality, and even speaks his own replies out loud.

| Layer | Tech |
|-------|------|
| Web UI (optional) | Django 5 + template (`/interface/templates/chat.html`) |
| API / Socket | FastAPI mounted in the same ASGI app |
| LLM backend | OpenAI Assistants API (optionally fine-tuned GPT-4o model) |
| Text-to-Speech | Azure Speech SDK |
| Deployment | Heroku (Procfile, Aptfile, runtime.txt) |

---

## ✨ Features

* **/api/chat** – POST an audience message, get Tony’s JSON reply; voice is synthesised asynchronously via Azure TTS. :contentReference[oaicite:0]{index=0}  
* **Assistant wrapper** – `framework/agents.py` wraps OpenAI β Assistants, handles thread creation, message routing, fine-tune jobs, and file uploads. :contentReference[oaicite:1]{index=1}  
* **Streaming personality** – the default fine-tuning dataset (see `converter.py`) shapes Tony as a crypto-degenerate Twitch streamer. :contentReference[oaicite:2]{index=2}  
* **Speech output** – single call to Azure `SpeechSynthesizer` (voice `en-US-DustinMultilingualNeural`). :contentReference[oaicite:3]{index=3}  
* **Heroku-ready** – Gunicorn + Uvicorn worker; ALSA libs pre-installed for audio playback inside dynos. :contentReference[oaicite:4]{index=4}  

---

## 🗂️ Project layout

