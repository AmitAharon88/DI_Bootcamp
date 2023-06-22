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

// Other way to do it- With bonus

// const allPlanets = [
//   {
//       namePlanet : "Earth",
//       color : "lightblue",
//       moons : 1
//   },
//   {
//       namePlanet : "Venus",
//       color : "pink",
//       moons : 3
//   },
//   {
//       namePlanet : "Jupiter",
//       color : "orange",
//       moons : 6
//   },
//   {
//       namePlanet : "Uranus",
//       color : "grey",
//       moons : 2
//   }
// ]

// function addPlanet () {
//   const section = document.querySelector(".listPlanets");

//   for (let planet of allPlanets){
//       const divPlanet = document.createElement("div");
//       divPlanet.classList.add("planet");

//       const text = document.createTextNode(planet["namePlanet"]);
//       divPlanet.appendChild(text)

//       divPlanet.style.backgroundColor = planet["color"];
//       section.appendChild(divPlanet);

//       addMoon(planet, section)

//   }
// }

// addPlanet()

// function addMoon (planet, section) {
//   let counter = 10;

//   for (let i = 0; i < planet["moons"] ; i++){
//       const divMoon = document.createElement("div");
//       divMoon.classList.add("moon");
//       divMoon.style.left = `${counter}rem`;
//       counter += 5;
//       section.appendChild(divMoon);
//   }
// }
