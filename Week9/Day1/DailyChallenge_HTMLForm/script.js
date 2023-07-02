const myForm = document.forms.myForm;
let previousP;
myForm.addEventListener('submit', (event) => {
    event.preventDefault()
    const elementFN = document.getElementById('firstName').value;
    const elementLN = document.getElementById('lastName').value;

    // Create a JavaScript object
    const inputData = {
        firstName: elementFN,
        lastName: elementLN
    };

    const JSONString = JSON.stringify(inputData, null, 2);

    const newP = document.createElement('p');
    const newData = document.createTextNode(JSONString);
    newP.appendChild(newData);

    if (previousP) {
        document.body.removeChild(previousP);
    }

    document.body.appendChild(newP);

    previousP = newP;
});