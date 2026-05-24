# Franklin Create

A clean MVP for a SOC2-style questionnaire prototype.

## Overview
This repository contains a minimal FastAPI backend and an Open WebUI frontend framework. Open WebUI is included as a Docker service, but no Ollama model runner is connected yet.

## Build and run
From the repository root:

```bash
docker compose build
docker compose up
```

Then open the frontend at `http://localhost:3000`.

### Services
- Backend API: `http://localhost:8000`
- Open WebUI frontend: `http://localhost:3000`

Open WebUI is configured as the UI layer via `ghcr.io/open-webui/open-webui:main`. The UI starts with the framework in place, and the model backend can be connected later by setting `OLLAMA_BASE_URL`, `OPENAI_API_KEY`, or another supported runner.

## Run locally without Docker

### Backend

```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py
```

The backend will run on `http://0.0.0.0:8000`.

## Project contents
- `backend/` — FastAPI app and Dockerfile
- `landing/` — static marketing/demo landing page
- `docker-compose.yml` — local development compose stack with Open WebUI frontend

## Landing page

Open `landing/index.html` in a browser to click through the product landing page and demo preview. The video modal currently uses a placeholder poster image; replace that modal content with an MP4 or hosted embed when a recorded walkthrough is ready.

## Notes
- Open WebUI is included as the frontend framework, but no Ollama or other model endpoint is configured yet.
- Use `docker compose down` to stop and remove containers.
- Connect a model later by updating `docker-compose.yml` with `OLLAMA_BASE_URL`, `OPENAI_API_KEY`, or another supported runtime.
