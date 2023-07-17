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

// BELOW NOT SURE IF ON THE RIGHT PATH

// Use javascript to retrieve the inputs and fetch your
// server for the register and login routes.
// const add = async () => {
//     const firstName = document.getElementById("firstName").value;
//     const lastName = document.getElementById("lastName").value;
//     const email = document.getElementById("email").value;
//     const usernameR = document.getElementById("usernameR").value;
//     const passwordR = document.getElementById("passwordR").value;
//     try {
//          const res = await fetch("/register", {
//               method: "POST",
//               headers: {
//                    "content-type": "application/json",
//               },
//               body: JSON.stringify({ 
//                 firstName: firstName, 
//                 lastName: lastName,
//                 email: email,
//                 username: usernameR,
//                 password: passwordR
//              }),
//          });
//          const data = await res.json();
//          render(data);
//     } catch (err) {
//          console.log(err);
//     }
//     };
    
    
//     // add render if not already in the code
//     const render = (arr) => {
//         const div = document.getElementById('response');
//         div.textContent = ""; // Clear previous response

//     const html = arr.map((item) => {
//          return `<div style="display:inline-block;margin:20px;padding:20px;border:1px solid #ccc;">
//               <h2>${item.name}</h2>
//               <h4>${item.price}</h4>
//          </div>`;
//     });
//     document.getElementById("root").innerHTML = html.join("");
//     };
    