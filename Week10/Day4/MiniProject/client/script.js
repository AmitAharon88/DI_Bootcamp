const loginInputs = document.getElementsByClassName('loginInput');
const loginBtn = document.querySelector('#loginBtn');

for (let input of loginInputs) {
    input.addEventListener("input", () => {
        let anyEmptyInput = false;
        for (let input of loginInputs) {
            if (input.value === "") {
                anyEmptyInput = true;
                break;
            }
        }
        loginBtn.disabled = anyEmptyInput;
    }
)};

const registerInputs = document.getElementsByClassName('registerInput');
const registerBtn = document.querySelector('#registerBtn');

for (let input of registerInputs) {
    input.addEventListener("input", () => {
        let anyEmptyInput = false;
        for (let input of registerInputs) {
            if (input.value === "") {
                anyEmptyInput = true;
                break;
            }
        }
        registerBtn.disabled = anyEmptyInput;
    }
)};


// Use javascript to retrieve the inputs and fetch your
// server for the register and login routes.
const firstName = document.getElementById("firstName");
const lastName = document.getElementById("lastName");
const email = document.getElementById("email");
const username = document.getElementById("usernameR");
const password = document.getElementById("passwordR");
const registerMessage = document.getElementById("message2")

async function register (e) {
    e.preventDefault();
   const registerInfo = {fname: firstName.value, lname: lastName.value, email: email.value, username: username.value, password: password.value}
    try {
         const res = await fetch("http://localhost:3000/register", {
              method: "POST",
              headers: {
                   "content-type": "application/json",
              },
              body: JSON.stringify(registerInfo),
         })
         const data = await res.json();
         if (res.status === 200) {
            registerMessage.innerText = data.message
         } else {
            registerMessage.innerText = data.error
         }
    } catch (err) {
         console.log(err);
    };
};
    
registerBtn.addEventListener("click", register);



const loginUsername = document.getElementById("usernameL");
const loginPassword = document.getElementById("passwordL");
const loginMessage = document.getElementById("message1")


async function login (e) {
    e.preventDefault();
   const loginInfo = {username: loginUsername.value, password: loginPassword.value}
    try {
         const res = await fetch("http://localhost:3000/login", {
              method: "POST",
              headers: {
                   "content-type": "application/json",
              },
              body: JSON.stringify(loginInfo),
         })
         const data = await res.json();
         if (res.status === 200) {
            loginMessage.innerText = data.message
         } else {
            loginMessage.innerText = data.error
         }
    } catch (err) {
         console.log(err);
    };
};

loginBtn.addEventListener("click", login);