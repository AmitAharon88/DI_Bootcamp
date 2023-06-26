setTimeout(hello, 2000);

function hello() {
  alert("Hello World");
}


setTimeout(addParagraph, 2000);

function addParagraph() {
  const divElem = document.getElementById('container');
  const pElem = document.createElement('p');
  const pText = document.createTextNode('Hello World')

  pElem.appendChild(pText);
  divElem.appendChild(pElem);
}


const newParagraph = setInterval(addParagraph, 2000);

function addParagraph() {
    const divElem = document.getElementById('container');
    const pElem = document.createElement('p');
    const pText = document.createTextNode('Hello World');
  
    pElem.appendChild(pText);
    divElem.appendChild(pElem);

    const pElements = document.querySelectorAll('p');
    if (pElements.length === 5) {
        clearInterval(newParagraph);
    }
}


// const button = document.querySelector('button');
// button.addEventListener('click', function() {
//     clearInterval(newParagraph);
// });

