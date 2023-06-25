// 🌟 Exercise 1 : Change The Article

const h1Elem = document.querySelector("h1");
console.log(h1Elem);

const articleElem = document.querySelector("article");
const lastParagraph = articleElem.lastElementChild;
articleElem.removeChild(lastParagraph)

const h2Elem = document.querySelector("h2");
h2Elem.addEventListener('click', backgroundColorChange);

function backgroundColorChange() {
    h2Elem.style.backgroundColor = 'red'
}

const h3Elem = document.querySelector("h3");
h3Elem.addEventListener('click', hideElem);

function hideElem() {
    h3Elem.style.display = 'none';
}

const buttonElem = document.querySelector('button');
buttonElem.addEventListener('click', makeBold);

function makeBold() {
    document.body.style.fontWeight = '900';
}

h1Elem.addEventListener('mouseover', changeFontSize);

function changeFontSize() {
    h1Elem.style.fontSize = '5px';
}

// Can't get this one to work
h2Elem.addEventListener('mouseover', fadeOut);

function fadeOut() {
    h2Elem.classList.add('fade-out');
}
