const divElement = document.getElementById("navBar");
divElement.setAttribute("id", "socialNetworkNavigation");

const container = document.body.querySelector("div ul");
const newIl = document.createElement("il");
const content = document.createTextNode("Logout");
newIl.appendChild(content);
container.appendChild(newIl);

console.log(container.firstElementChild.textContent);
console.log(container.lastElementChild.textContent);
