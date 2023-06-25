// 🌟 Exercise 3 : Transform The Sentence

let allBoldItems;

function getBoldItems() {
  allBoldItems = document.querySelectorAll("strong");
}

getBoldItems();
console.log(allBoldItems);

for (let item of allBoldItems) {
    item.addEventListener('mouseover', highlight);
    item.addEventListener('mouseout', returnItemsToDefault);
}

function highlight(e) {
    e.target.style.color = "blue";
}

function returnItemsToDefault(e) {
    e.target.style.color = "black";
}