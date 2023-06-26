const divElem = document.querySelector("div");

divElem.addEventListener("click", function () {
  alert(`I am not a button`);
});

// Not sure why this one doesnt work
divElem.addEventListener("dblclick", function () {
  alert(`Double clicking doesn't change the fact that I am not a button!`);
});

divElem.addEventListener("mouseover", function () {
  document.body.style.backgroundColor = "lightblue";
});

divElem.addEventListener('mouseout', function () {
    document.body.style.backgroundColor = 'lightpink';
  });

document.body.addEventListener('copy', function () {
    divElem.style.fontWeight = "900";
  });

document.body.addEventListener('keypress', function () {
    divElem.style.fontSize = "200px";
  });
