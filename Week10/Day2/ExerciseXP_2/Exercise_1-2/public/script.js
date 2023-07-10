async function getUser() {
    try {
        const response = await fetch('/users')
        if(response.ok) {
            const data = await response.json();
            // its not be console. lodded or added to the page
            console.log(data);
            document.getElementById("data").textContent = JSON.stringlify(data);
        } else {
            throw new Error ("issue with fetch");
        }
    } catch (error) {
        console.log(error);
    }
};

getUser()