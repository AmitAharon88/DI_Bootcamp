const form = document.forms[0];
console.log(form);

form.addEventListener("submit", getValuesForm);

function getValuesForm(event) {
    event.preventDefault();
    const firstNameInput = document.getElementById('fname');
    const lastNameInput = document.getElementById('lname');
    console.log(firstNameInput.value);
    console.log(lastNameInput.value);
}

form.addEventListener("submit", getValuesForm2);

function getValuesForm2(event) {
    event.preventDefault(); // Used so the input wont be cleared from the form
    const firstNameInput2 = form.elements.firstname.value;
    const lastNameInput2 = form.elements.lastname.value;
    console.log(firstNameInput2);
    console.log(lastNameInput2);
    addNameList(firstNameInput2, lastNameInput2)
}

function addNameList(firstName, lastName) {
    const ulElem = document.querySelector('ul');
    const firstNameIl = document.createElement('li');
    const firstNameIlText = document.createTextNode(firstName)
    const lastNameIl = document.createElement('li');
    const lastNameIlText = document.createTextNode(lastName)

    firstNameIl.appendChild(firstNameIlText);
    lastNameIl.appendChild(lastNameIlText);
    ulElem.appendChild(firstNameIl);
    ulElem.appendChild(lastNameIl);
}