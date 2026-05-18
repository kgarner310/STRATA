# STRATA

AI reasoning engine for commercial insurance producers. Analyzes accounts to detect exposures, frame submissions, explain coverage gaps, and generate producer talking points.

## Quick Start

### Prerequisites

- Python 3.12+
- Node.js 20+
- Docker & Docker Compose (for PostgreSQL)

### 1. Start the database

```bash
docker-compose up db -d
```

### 2. Set up the backend

```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install dependencies
pip install -e ".[dev]"

# Run migrations
alembic upgrade head

# Seed initial users only
python -m app.seeds.seed_all

# Start the API
uvicorn app.main:app --reload
```

### 3. Set up the frontend

```bash
cd frontend
cp .env.local.example .env.local
npm install
npm run dev
```

### 4. Open the app

Navigate to http://localhost:3000 and log in with an account you created or seeded locally.

## Full Stack with Docker

```bash
docker-compose up --build
```

This starts PostgreSQL, the FastAPI backend, and the Next.js frontend. Then run migrations and create initial users:

```bash
docker-compose exec api alembic upgrade head
docker-compose exec api python -m app.seeds.seed_all
```

## Architecture

### Backend (FastAPI + SQLAlchemy 2.0)

- **Auth**: Session tokens in HTTP-only cookies with RBAC (admin/producer/viewer)
- **4 Analysis Pillars**: Account Analysis, Coverage Reasoning, Submission Strategy, Market Intelligence
- **Parking Lot Brief**: 10-second prep synthesized from all 4 pillars
- **LLM**: Model-agnostic client (Anthropic / OpenAI / Mock) -- mock mode works without API keys
- **Audit**: Full audit logging of all mutating operations

### Frontend (Next.js + Tailwind + shadcn/ui)

- **Account Workspace**: 2x2 panel grid (desktop) / collapsible accordion (mobile)
- **TanStack Query**: Cached data fetching with background refresh
- **Responsive**: Full mobile support

### API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| POST | /api/v1/auth/login | Login (sets cookie) |
| POST | /api/v1/auth/logout | Logout |
| GET | /api/v1/auth/me | Current user |
| POST | /api/v1/accounts/intake | Create account |
| GET | /api/v1/accounts | List accounts |
| GET | /api/v1/accounts/:id | Get account |
| GET | /api/v1/analysis/:id | Account analysis |
| GET | /api/v1/coverage/gaps/:id | Coverage gaps |
| GET | /api/v1/strategy/submission/:id | Submission strategy |
| GET | /api/v1/market/intel/:id | Market intelligence |
| GET | /api/v1/brief/parking-lot/:id | Parking lot brief |

## Test Accounts

Demo accounts are no longer seeded by default. Create a real account through intake, then run STRATA analysis.

## Tests

```bash
pip install -e ".[dev]"
python -m pytest tests/ -v
```

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| DATABASE_URL | required | PostgreSQL connection string |
| SECRET_KEY | required | Session signing key |
| LLM_PROVIDER | anthropic | "anthropic", "openai", or "mock" |
| ANTHROPIC_API_KEY | - | Required if provider is anthropic |
| OPENAI_API_KEY | - | Required if provider is openai |
| DEBUG | false | Enable debug mode |
| CORS_ORIGINS | ["http://localhost:3000"] | Allowed CORS origins |

## Live LLM smoke test

```bash
LLM_PROVIDER=anthropic ANTHROPIC_API_KEY=... python scripts/live_smoke.py
```

On PowerShell:

```powershell
$env:LLM_PROVIDER="anthropic"
$env:ANTHROPIC_API_KEY="..."
.\.venv\Scripts\python.exe scripts\live_smoke.py
```
