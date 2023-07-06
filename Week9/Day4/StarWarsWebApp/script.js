
function getIndex () {
    let randomNumber = 0 ;
    let otherNumber = 0;
    do {
        otherNumber = Math.floor(Math.random() * 84) + 1;
    } while (randomNumber === otherNumber)

    randomNumber = otherNumber
    getData(randomNumber);
};

function button () {
    const button = document.querySelector("button")
    button.addEventListener("click", () => {
        // const i = document.querySelector('i')
        // console.log(i)
        // // i.style.display = 'block'
        getIndex()
    })
};

async function getData(i) {
    try {
        const response = await fetch(`https://www.swapi.tech/api/people/${i}`)
        if(response.ok) {
            const dataObj= await response.json();
            const personObject= dataObj['result']['properties']
            console.log(personObject)
            const response2 = await fetch(personObject['homeworld'])
            const homeWorldObj= await response2.json();
            const homeWorldDetails= homeWorldObj['result']['properties']
            displayPerson(personObject, homeWorldDetails)
        } else {
            throw new Error ("Oh no! That person isn't availible")
        }
    } catch (error) {
        console.log(error.message)
    }
};

function addDOM (item) {
    const divElement = document.body.querySelector('div');
    const p = document.createElement('p');
    const pText = document.createTextNode(item);
    p.appendChild(pText);
    divElement.appendChild(p);
};

function displayPerson (personObj, homeWorld) {
    const pElements = document.querySelectorAll('p');
    pElements.forEach(pElement => pElement.parentNode.removeChild(pElement));

    const {name, height, birth_year} = personObj;
    const personDetails = {name, height, birth_year};
    for (let item in personDetails) {
        addDOM(`${item}:  ${personDetails[item]}`);
    };

    const homeWorldName = homeWorld['name'];
    addDOM(`home world:  ${homeWorldName}`);

};

button()







