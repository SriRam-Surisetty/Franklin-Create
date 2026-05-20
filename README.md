# Franklin Create

A clean MVP for a SOC2-style questionnaire prototype.

## Overview
This repository contains a minimal FastAPI backend and a tiny static frontend. The project is built to run locally with Docker Compose.

## Run (recommended)
From the repository root:

```bash
docker compose up --build
```

Then open the frontend at `http://localhost:3000`.

### Services
- Backend API: `http://localhost:8000`
- Frontend: `http://localhost:3000`

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

### Frontend

```bash
python -m http.server 3000 --directory frontend
```

Open `http://localhost:3000` in your browser.

## Project contents
- `backend/` — FastAPI app and Dockerfile
- `frontend/` — static HTML frontend, Dockerfile, questionnaire content
- `docker-compose.yml` — local development compose stack

## Test questionnaire
The sample questionnaire is available at `frontend/questionnaire.md`.

## Notes
- This MVP does not require Ollama or Qdrant.
- Use `docker compose down` to stop and remove containers.
