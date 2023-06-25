const form = document.forms[0];
form.addEventListener("submit", getValuesForm);

function getValuesForm (event) {
    event.preventDefault(); //stop the form from refreshing the page
    const valueRadius = parseFloat(event.target.radius.value);
    getVolume(valueRadius);
}

function getVolume (radius) {
    const pi = Math.PI;
    const volume = (3/4) * pi * radius ** 3;
    form.volume.value = volume.toFixed(2);
}