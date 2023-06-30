const robots = [
  {
    id: 1,
    name: "Leanne Graham",
    username: "Bret",
    email: "Sincere@april.biz",
    image: "https://robohash.org/1?200x200",
  },
  {
    id: 2,
    name: "Ervin Howell",
    username: "Antonette",
    email: "Shanna@melissa.tv",
    image: "https://robohash.org/2?200x200",
  },
  {
    id: 3,
    name: "Clementine Bauch",
    username: "Samantha",
    email: "Nathan@yesenia.net",
    image: "https://robohash.org/3?200x200",
  },
  {
    id: 4,
    name: "Patricia Lebsack",
    username: "Karianne",
    email: "Julianne.OConner@kory.org",
    image: "https://robohash.org/4?200x200",
  },
  {
    id: 5,
    name: "Chelsey Dietrich",
    username: "Kamren",
    email: "Lucio_Hettinger@annie.ca",
    image: "https://robohash.org/5?200x200",
  },
  {
    id: 6,
    name: "Mrs. Dennis Schulist",
    username: "Leopoldo_Corkery",
    email: "Karley_Dach@jasper.info",
    image: "https://robohash.org/6?200x200",
  },
  {
    id: 7,
    name: "Kurtis Weissnat",
    username: "Elwyn.Skiles",
    email: "Telly.Hoeger@billy.biz",
    image: "https://robohash.org/7?200x200",
  },
  {
    id: 8,
    name: "Nicholas Runolfsdottir V",
    username: "Maxime_Nienow",
    email: "Sherwood@rosamond.me",
    image: "https://robohash.org/8?200x200",
  },
  {
    id: 9,
    name: "Glenna Reichert",
    username: "Delphine",
    email: "Chaim_McDermott@dana.io",
    image: "https://robohash.org/9?200x200",
  },
  {
    id: 10,
    name: "Clementina DuBuque",
    username: "Moriah.Stanton",
    email: "Rey.Padberg@karina.biz",
    image: "https://robohash.org/10?200x200",
  },
];

let robotSearch = [];

function createRobot() {
  robotSearch = robots.map((element) => {
    const { name, email, image } = element;
    // create card
    const divOuterElement = document.createElement("div");
    const imgElement = document.createElement("img");
    const divInnerElement = document.createElement("div");
    const pOneElement = document.createElement("p");
    const pTwoElement = document.createElement("p");
    // create class
    divOuterElement.classList.add('card')
    imgElement.classList.add('image')
    divInnerElement.classList.add('textBox')
    pOneElement.classList.add('name')
    pTwoElement.classList.add('email')

    // create text
    const robotName = document.createTextNode(name);
    const robotEmail = document.createTextNode(email);
    // add text and image to card
    pOneElement.appendChild(robotName);
    pTwoElement.appendChild(robotEmail);
    imgElement.setAttribute("src", image);
    // add  card to body
    const sectionElement = document.querySelector('section');
    sectionElement.appendChild(divOuterElement);
    divOuterElement.appendChild(imgElement);
    divOuterElement.appendChild(divInnerElement);
    divInnerElement.appendChild(pOneElement);
    divInnerElement.appendChild(pTwoElement);
    return { name, email, image, element: divOuterElement };
  });
}

createRobot(robots);

// adding autosearch
const searchInput = document.querySelector("input");
searchInput.addEventListener("input", (e) => {
  const value = e.target.value.toLowerCase();
  robotSearch.forEach((robot) => {
    const isVisible =
      robot.name.toLowerCase().includes(value) ||
      robot.email.toLowerCase().includes(value);
    // if any of the conditions above is true then set isVisible to true
    robot.element.classList.toggle("hide", !isVisible);
  });
});
