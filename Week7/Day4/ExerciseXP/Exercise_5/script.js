// 2.
const divElement = document.querySelector("div");
console.log(divElement);

const ulElement = document.querySelector("ul");
ulElement.children[1].textContent = "Richard";

const ulElements = document.querySelectorAll("ul");
const secondUl = ulElements[1];
const liElements = secondUl.querySelectorAll("li");
const secondLi = liElements[1];
secondUl.removeChild(secondLi);

for (let i = 0; i < ulElements.length; i++) {
  const liElement = ulElements[i].querySelector("li");
  liElement.textContent = "Amit";
}

// 3.
for (let i = 0; i < ulElements.length; i++) {
  ulElements[i].classList.add("student_list");
}

// ulElement defined above
ulElement.classList.add("university", "attendance");

// 4.
divElement.style.backgroundColor = "lightblue";

const liElements2 = document.querySelectorAll("li");
for (const item of liElements2) {
  if (item.textContent === "Dan") {
    item.style.display = "none";
  } else {
    continue;
  }
}

// ulElement defined above
ulElement.children[1].style.border = "2px solid red";

document.body.style.fontFamily = "Helvetica";

// Bonus:
const ulParent = document.querySelector("ul");
const names = ulParent.querySelectorAll("li");

if ((divElement.style.backgroundColor = "lightblue")) {
  const firstName = names[0].textContent;
  const secondName = names[1].textContent;
  alert(`Hello ${firstName} and ${secondName}!`);
}
