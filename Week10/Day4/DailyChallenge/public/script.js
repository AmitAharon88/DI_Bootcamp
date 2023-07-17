const inputs = document.querySelectorAll('input');
const btn = document.querySelector('button');

for (let input of inputs) {
    input.addEventListener("input", () => {
        let anyEmptyInput = false;
        for (let input of inputs) {
            if (input.value === "") {
                anyEmptyInput = true;
                break;
            }
        }
        btn.disabled = anyEmptyInput;
    }
)};

// Register form submission
const formRegister = document.getElementById('registerForm');
formRegister.addEventListener('submit', registerUser);

async function registerUser (e) {
    e.preventDefault();
    const data = new FormData(formRegister);
    const objData = Object.fromEntries(data);

    const responsePost = await fetch('/registeruser', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(objData)
});

    if (responsePost.ok) {
      const result = await responsePost.json();
      const div = document.getElementById('response');
      div.textContent = result;
    }
};

// Login form submission
const formLogin = document.getElementById('loginForm');
formLogin.addEventListener('submit', loginUser);

async function loginUser (e) {
    e.preventDefault();
    const data = new FormData(formLogin);
    const objData = Object.fromEntries(data);

    const responsePost = await fetch('/loginuser', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(objData)
});

    if (responsePost.ok) {
      const result = await responsePost.json();
      const div = document.getElementById('response');
      div.textContent = result;
    }
};



    
  


