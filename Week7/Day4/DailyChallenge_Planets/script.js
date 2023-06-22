// 1.
const planets = [
  "Mercury",
  "Venus",
  "Earth",
  "Mars",
  "Jupiter",
  "Saturn",
  "Uranus",
  "Neptune",
  "Pluto",
];

const moons = {
  Mercury: 0,
  Venus: 0,
  Earth: 1,
  Mars: 2,
  Jupiter: 79,
  Saturn: 82,
  Uranus: 27,
  Neptune: 14,
  Pluto: 5,
};

const container = document.querySelector(".listPlanets");

for (const planet of planets) {
  // Create the element
  const div = document.createElement("div");
  // Create the class
  div.classList.add("planet", planet);
  // Create the content of the div
  const text = document.createTextNode(planet);
  // add the paragraph to the div
  container.appendChild(div);
  // add the text to the div
  div.appendChild(text);

  if (div.classList.contains("Mercury")) {
    div.style.backgroundColor = "darkred";
  } else if (div.classList.contains("Venus")) {
    div.style.backgroundColor = "brown";
  } else if (div.classList.contains("Earth")) {
    div.style.backgroundColor = "green";
  } else if (div.classList.contains("Mars")) {
    div.style.backgroundColor = "red";
  } else if (div.classList.contains("Jupiter")) {
    div.style.backgroundColor = "purple";
  } else if (div.classList.contains("Saturn")) {
    div.style.backgroundColor = "tan";
  } else if (div.classList.contains("Uranus")) {
    div.style.backgroundColor = "blue";
  } else if (div.classList.contains("Neptune")) {
    div.style.backgroundColor = "white";
  } else if (div.classList.contains("Pluto")) {
    div.style.backgroundColor = "silver";
  }
}
