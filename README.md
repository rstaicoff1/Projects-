# Friend Matcher 

This project is a simple web app that matches fans of the same pro team within 50 km.
It is intentionally small and easy to understand.

## Run it

1. Create a virtualenv and install deps:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Start the server:

```bash
python app.py
```

3. Open `http://127.0.0.1:5000` in your browser.

## File-by-file learning map

### `app.py`

What it does:
- Loads/saves people to a JSON file.
- Calculates distance with Haversine.
- Calculates a fan score from answers.
- Matches profiles by team, distance, and score.

### `templates/index.html`

What it does:
- Collects user name, team, location, and 4 fan questions.
- Submits the form via JavaScript.

### `static/app.js`

What it does:
- Reads form values.
- Sends data to `/api/profile` and `/api/match`.
- Updates the page with the match.

### `static/styles.css`

What it does:
- Simple styling for layout and inputs.

### `data/people.json`

What it does:
- Stores all profiles in a local JSON list.  
ide you step by step.
If any part feels too hard, ask and I can give you the exact code.
