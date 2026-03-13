const form = document.querySelector("#profile-form");
const resultCard = document.querySelector("#result");
const output = document.querySelector("#match-output");

function getAnswers(data) {
  return [
    Number(data.get("q1")),
    Number(data.get("q2")),
    Number(data.get("q3")),
    Number(data.get("q4")),
    Number(data.get("q5")),
    Number(data.get("q6")),
  ];
}

form.addEventListener("submit", async (e) => {
  e.preventDefault();

  const data = new FormData(form);
  const answers = getAnswers(data);
  const profile = {
    name: data.get("name"),
    team: data.get("team"),
    lat: Number(data.get("lat")),
    lon: Number(data.get("lon")),
    answers,
  };

  const invalid = answers.some((a) => Number.isNaN(a) || a < 1 || a > 5);
  if (!profile.name || !profile.team || invalid) {
    resultCard.hidden = false;
    output.textContent = "Please fill all fields and keep answers between 1 and 5.";
    return;
  }
  // Step 1: save profile on the server
  const created = await fetch("/api/profile", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(profile),
  }).then((r) => r.json());

  // Step 2: request a match
  const matched = await fetch("/api/match", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ profile: created.profile }),
  }).then((r) => r.json());

  const match = matched.match;
  resultCard.hidden = false;

  if (!match) {
    output.textContent = "No match yet. Try again later.";
    return;
  }

  output.innerHTML = `
    <p><strong>Name:</strong> ${match.name}</p>
    <p><strong>Team:</strong> ${match.team}</p>
    <p><strong>Fan score:</strong> ${match.score}</p>
  `;
});
