from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from flask import Flask, jsonify, render_template, request

APP_DIR = Path(__file__).parent
DATA_FILE = APP_DIR / "data" / "people.json"

app = Flask(__name__)


def load_people() -> List[Dict[str, Any]]:
    if not DATA_FILE.exists():
        return []
    with DATA_FILE.open("r", encoding="utf-8") as f:
        return json.load(f)


def save_people(people: List[Dict[str, Any]]) -> None:
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    with DATA_FILE.open("w", encoding="utf-8") as f:
        json.dump(people, f, indent=2)


# Haversine distance in kilometers
# TODO: Try implementing this yourself as an exercise.
# Alternative: Use geopy.distance if you want a library version.

def distance_km(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    r = 6371.0
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)

    a = math.sin(dphi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return r * c


# Fan score: simple sum of answers 1-5
# TODO: Replace with a smarter weighting scheme.

def fan_score(answers: List[int]) -> int:
    total = sum(answers)
    max_score = len(answers) * 5
    return int(total / max_score * 100)
    


# Matching: same team, within 50km, closest score
# TODO: Replace with a ranking algorithm (distance + score diff).

def find_match(profile: Dict[str, Any], people: List[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
    best: Optional[Tuple[Dict[str, Any], float, int]] = None
    for other in people:
        if other["name"].strip().lower() == profile["name"].strip().lower():
            continue
        if other["team"].strip().lower() != profile["team"].strip().lower():
            continue
        d = distance_km(profile["lat"], profile["lon"], other["lat"], other["lon"])
        if d > 50:
            continue
        score_diff = abs(profile["score"] - other["score"])
        # pick smallest score diff, then closest distance
        rank = (score_diff * 2) + (d * 0.5)
        if best is None or rank < best[1] and best[2] > score_diff:
            best = (other, rank, score_diff)
    return best[0] if best else None    
   


@app.get("/")
def index():
    return render_template("index.html")


@app.post("/api/profile")
def create_profile():
    data = request.get_json(force=True)

    profile = {
        "name": data.get("name", "").strip(),
        "team": data.get("team", "").strip(),
        "lat": float(data.get("lat")),
        "lon": float(data.get("lon")),
        "answers": [int(x) for x in data.get("answers", [])],
    }
    profile["score"] = fan_score(profile["answers"])

    people = load_people()
    people.append(profile)
    save_people(people)

    return jsonify({"ok": True, "profile": profile})


@app.post("/api/match")
def match():
    data = request.get_json(force=True)
    profile = data["profile"]

    people = load_people()
    match_profile = find_match(profile, people)

    return jsonify({"ok": True, "match": match_profile})


if __name__ == "__main__":
    app.run(debug=True)
