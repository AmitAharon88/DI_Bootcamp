async function getGif(category) {
    try {
        const response = await fetch(`https://api.giphy.com/v1/gifs/search?q=${category}&
        rating=g&limit=1&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My`)
        if(response.ok) {
            const gifObj = await response.json(); //PROMISE
            console.log(gifObj);
            addContent(gifObj);
        } else {
            throw new Error ("Issue with fetch")
        }
    } catch (error) {
        console.log(error.message)
    }
};

function getCategory() {
    const form = document.forms[0];
    form.addEventListener('submit', (event) => {
        event.preventDefault();
        const categoryInput = document.getElementById('categoryInput');
        const category = categoryInput.value;
        getGif(category);
    })
};

function addContent(object) {
    const div = document.createElement("div");
    const image = document.createElement("img");
    const button = document.createElement("button");
    const urlGif = object["data"][0]['images']['original']["url"];
    const buttonText = document.createTextNode('Delete');

    document.body.appendChild(div);
    div.appendChild(image);
    image.src = urlGif;
    div.appendChild(button);
    button.type = 'button';
    button.classList.add('delete');
    button.appendChild(buttonText);
    deleteOne(image, div, button);
    deleteAll();
};

function deleteOne(image, parent, button) {
    button.addEventListener('click', () => {
        parent.removeChild(image);
        parent.removeChild(button);
    });
};
 // can't get olt the delete button to be removed.
//  if i do document.querySelectorAll('button'), i end up deleteing all the buttons including the submit button.

function deleteAll() {
    const allImages = document.querySelectorAll('img')
    const allButtons = document.querySelectorAll('.delete');
    console.log(allButtons)
    if (allImages.length === 2) {
        const div = document.createElement("div");
        const button = document.createElement("button");
        const buttonText = document.createTextNode('Delete All');
        button.type = 'button';
        button.classList.add('delete')
        document.body.appendChild(div);
        div.appendChild(button);
        button.appendChild(buttonText);
        div.style.position = 'fixed';
        div.style.top = '10px';
        div.style.left = '250px';

        button.addEventListener('click', () => {
            allImages.forEach(image => image.parentNode.removeChild(image));
            allButtons.forEach(buttom => buttom.parentNode.removeChild(buttom));
        })
    }
};

getCategory();