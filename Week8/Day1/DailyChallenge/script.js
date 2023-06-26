const form = document.forms[0];
form.addEventListener("submit", getValuesForm);

function getValuesForm(event) {
  event.preventDefault();
  const noun = document.getElementById("noun").value;
  const adjective = document.getElementById("adjective").value;
  const person = document.getElementById("person").value;
  const verb = document.getElementById("verb").value;
  const place = document.getElementById("place").value;

  if (
    noun === "" ||
    adjective === "" ||
    person === "" ||
    verb === "" ||
    place === ""
  ) {
    alert("Please fill in all the fields.");
    return;
  } else if (
    containsNumber(noun) ||
    containsNumber(adjective) ||
    containsNumber(person) ||
    containsNumber(verb) ||
    containsNumber(place)
  ) {
    alert("Invalid Input. Please enter valid text with letters only.");
    return;
  } else {
    addStory(noun, adjective, person, verb, place);
  }
}

function containsNumber(str) {
    return /\d/.test(str);
}

function addStory(noun, adjective, person, verb, place) {
  const spanElem = document.querySelector("span");
  const storyText = document.createTextNode(
    `Once upon a time, there was a ${adjective} ${noun} named ${person}. ${person} loved to ${verb} in ${place}. The end.`
  );
  spanElem.appendChild(storyText);
}


// OTher way to do it (better)- from class
// const myform = document.forms.libform
// myform.addEventListener("submit", getValues);

// function getValues(event) {
//     event.preventDefault();
//     let objValues = {}
//     const allInputs = event.target.querySelectorAll("input");
//     for (let inp of allInputs) {
//         if (inp.value === "") {
//             alert("fill the form - missing element")
//             return;
//         }
//         objValues[inp.id] = inp.value;
//     }
//     showStory(objValues)
// }

// function showStory (objValues) {
//     const spanElement = document.getElementById("story");
//     const text = `The ${objValues["noun"]} is ${objValues["verb"]} with ${objValues["person"]}`
//     const textNode = document.createTextNode(text)
//     spanElement.appendChild(textNode)
// }