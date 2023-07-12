async function getUser() {
    try {
        const response = await fetch('/users')
        if(response.ok) {
            const data = await response.json();
            console.log(data);
            document.getElementById("data").textContent = JSON.stringify(data);
        } else {
            throw new Error ("issue with fetch");
        }
    } catch (error) {
        console.log(error);
    }
};

getUser()