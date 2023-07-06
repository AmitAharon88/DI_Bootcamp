// Exercise 1: Giphy API
async function getData() {
    try {
        const response = await fetch(`https://api.giphy.com/v1/gifs/search?q=hilarious&rating=g&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My`)
        if(response.ok) {
            const dataObj = await response.json(); //PROMISE
            console.log(dataObj);
        } else {
            throw new Error ("Issue with fetch")
        }
    } catch (error) {
        console.log(error.message)
    }
};

getData();


// Exercise 2: Giphy API (Can't figure out how to make this work)
async function getGifs() {
    try {
        const response = await fetch(`https://api.giphy.com/v1/gifs/search?q=sun&rating=g&offset=2&limit=10&
        api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My`)
        if(response.ok) {
            const dataObj = await response.json(); //PROMISE
            console.log(dataObj['data']);
        } else {
            throw new Error ("Issue with fetch")
        }
    } catch (error) {
        console.log(error.message)
    }
};

getGifs();


// Exercise 3: Async Function

async function starWars () {
    try {
        const response = await fetch("https://www.swapi.tech/api/starships/9/")
        if(response.ok) {
            const starWarsObj = await response.json();
            console.log(starWarsObj.result)
        } else {
            throw new Error ("Issue with fetch")
        }
    } catch (error) {
        console.log(error.message)
    }
};

starWars();


// Exercise 4: Analyze

function resolveAfter2Seconds() {
    return new Promise(resolve => {
        setTimeout(() => {
            resolve('resolved');
        }, 2000);
    });
}

async function asyncCall() {
    console.log('calling');
    let result = await resolveAfter2Seconds();
    console.log(result);
}

asyncCall();


// Output:
// inside the async function it is synchronized. calling will be displayed first on the console then after 2 second the rexolve will appear.
