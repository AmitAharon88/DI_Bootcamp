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
const registerBtn = document.getElementById('registerBtn');
registerBtn.addEventListener('submit', async (e) => {
    e.preventDefault();
  
    const firstName = document.getElementById('firstName').value;
    const lastName = document.getElementById('lastName').value;
    const email = document.getElementById('email').value;
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
  
    const response = await fetch('/register', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ firstName, lastName, email, username, password })
    });
  
    const message = await response.text();
    const div = document.getElementById('response');
    div.textContent = ""; // Clear previous response

    if (message === 'register') {
      console.log('Registration successful');
      const divMessege = document.createTextNode(`Your account has now been created`);
      div.appendChild(divmessege);
    } else {
      const divMessege = document.createTextNode(`Username already exists`);
      div.appendChild(divMessege);
    };
});

// Login form submission
document.getElementById('loginForm').addEventListener('submit', async (e) => {
    e.preventDefault();
  
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
  
    const response = await fetch('/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ username, password })
    });
  
    const message = await response.text();
    const div = document.getElementById('response');
    div.textContent = ""; // Clear previous response

    if (message === 'login') {
        const divMessege = document.createTextNode(`Hi ${user.firstName}, welcome back`);
        div.appendChild(divMessege);
      } else {
        const divMessege = document.createTextNode(`Username is not registeres`);
        div.appendChild(divMessege);
      };
});