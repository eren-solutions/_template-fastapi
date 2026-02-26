# {{PROJECT_NAME}}

{{PROJECT_DESCRIPTION}}

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
uvicorn src.main:app --reload
```

## Test

```bash
pytest tests/ -v
```

## Docker

```bash
docker build -t {{PROJECT_NAME}} .
docker run -p 8000:8000 {{PROJECT_NAME}}
```
