# Nestday

Gentle day-rhythm and bedtime-routine ideas for new parents — education, not medical advice.

Quiz → personalized plan preview → paywall (founding list, **no real payments**).

## Run locally
```bash
pip install -r requirements.txt
python app.py   # http://127.0.0.1:5113
```

## Deploy (Render)
- Build: `pip install -r requirements.txt`
- Start: `gunicorn -b 0.0.0.0:$PORT app:app`
- Env: `SECRET_KEY`, `ADMIN_PASSWORD` (owner-only `/admin`), `DATABASE_URL` (pooled Neon Postgres URL), `DATABASE_SCHEMA=nestday`. Without `DATABASE_URL` it falls back to SQLite (`DATABASE_PATH`).

## Tests
```bash
pytest -q
```

Plans are deterministic rules in `nestday_brand.py` (`plan()`); swap in an LLM later if wanted.
With `DATABASE_URL` set, leads persist in Postgres. SQLite fallback on free hosting is ephemeral.
