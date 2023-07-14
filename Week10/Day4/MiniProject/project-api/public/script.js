const loginForm = document.getElementById('loginForm');
const usernameLogin = document.getElementById('usernameL');
const passwordLogin = document.getElementById('passwordL');



const loginBtn = document.getElementById('loginBtn');
const registerBtn = document.getElementById('registerBtn');

const addUser = async () => {
    const firstName = document.getElementById('firstName').value.trim();
    const lastName = document.getElementById('lastnName').value.trim();
    const email = document.getElementById('email').value.trim();
    const username = document.getElementById('usernameR').value.trim();
    const password = document.getElementById('passwordR').value.trim();
    try {
         const res = await fetch("/api/users", {
              method: "POST",
              headers: {
                   "content-type": "application/json",
              },
              body: JSON.stringify({
                first_name : firstName,
                last_name : lastName,
                email : email,
                username : username,
                password : password
              }),
         });
         const data = await res.json();
         render(data);
    } catch (err) {
         console.log(err);
    }
};
    













loginForm.addEventListener('input', function(event) {
    event.preventDefault();
    if (usernameInput.value.trim() !== '' && passwordInput.value.trim() !== '') {
        loginBtn.disabled = false;
    } else {
        loginBtn.disabled = true;
  }
});


loginBtn.addEventListener("submit", add);

const add = async (event) => {
    event.preventDefault();
    const loginData = {
        username: usernameInput.value.trim(),
        password: passwordInput.value.trim()
    }
    try {
         const res = await fetch("/login", {
              method: "POST",
              headers: {
                   "content-type": "application/json",
              },
              body: JSON.stringify(loginData),
         });
         const data = await res.json();
    } catch (err) {
         console.log(err);
    }
};

