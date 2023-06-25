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
