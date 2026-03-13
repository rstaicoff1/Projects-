# Friend Matcher (Learning-First)

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

Your tasks:
- Replace `fan_score()` with your own scoring logic.
- Improve `find_match()` to rank results by a weighted score.

Alternate examples:
- Score weighting:
  - Give Q1 and Q3 extra weight if "games watched" and "news follow" matter more.
  - Example formula idea: `score = 2*q1 + q2 + 2*q3 + q4`
- Matching formula:
  - Compute a combined ranking number: `rank = (score_diff * 2) + (distance_km * 0.5)`
  - Choose the profile with the lowest `rank`.

### `templates/index.html`

What it does:
- Collects user name, team, location, and 4 fan questions.
- Submits the form via JavaScript.

Your tasks:
- Add or remove questions (3-5 is fine).
- Replace numeric inputs with drop-downs or radio buttons.

Alternate examples:
- Use `select` inputs instead of numbers (1-5).
- Add a question about favorite player and include it in matching.

### `static/app.js`

What it does:
- Reads form values.
- Sends data to `/api/profile` and `/api/match`.
- Updates the page with the match.

Your tasks:
- Add validation (example: ensure all answers are 1-5).
- Show distance and score difference in the result.

Alternate examples:
- Use `Promise.all` to parallelize API calls.
- Cache the last profile in `localStorage` and pre-fill the form.

### `static/styles.css`

What it does:
- Simple styling for layout and inputs.

Your tasks:
- Change the font and color scheme.
- Add a small logo or header graphic.

Alternate examples:
- Use a bold sans-serif font.
- Add a colored banner behind the header.

### `data/people.json`

What it does:
- Stores all profiles in a local JSON list.

Your tasks:
- Reset this file to `[]` whenever you want a clean slate.
- Add a field like `created_at` and sort by recency.

## Next steps

If you want, tell me which file you want to work on first and I will guide you step by step.
If any part feels too hard, ask and I can give you the exact code.
