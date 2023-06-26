// 🌟 Exercise 1 : Scope

// #1
function funcOne() {
    let a = 5;
    if(a > 1) {
        a = 3;
    }
    alert(`inside the funcOne function ${a}`);
}

// a=3 so when running the fuction you will receive an alert - inside the funcOne fucntion 3

// #1.1 - run in the console:
funcOne()

// #1.2 What will happen if the variable is declared with const instead of let ?
// An error will occure as a string const variable cannot be redefined.

//#2
let  a = 0;
function funcTwo() {
    a = 5;
}

function funcThree() {
    alert(`inside the funcThree function ${a}`);
}
// a=0 as the reassigned a to 5 cannot be accessed without being the funTwo.

// // #2.1 - run in the console:
funcThree()     // 0
funcTwo()       // 5
funcThree()     // 5

// #2.2 What will happen if the variable is declared with const instead of let ?
// An error will occure when calling function funcTwo as a string const variable cannot be redefined.

//#3
function funcFour() {
    window.a = "hello";
}

function funcFive() {
    alert(`inside the funcFive function ${a}`);
}
// a= 'hello' as window.a make this a gloabl variable

// #3.1 - run in the console:
funcFour()      // a=hello
funcFive()      // I thouhg the following would apprear- inside the funcFive function hello, but it doesnt.

//#4
const a = 1;
function funcSix() {
    let a = "test";
    alert(`inside the funcSix function ${a}`);
}
// a=test

// #4.1 - run in the console:
funcSix()

// #4.2 What will happen if the variable is declared
// with const instead of let ?
// it still works and a = test

//#5
let a = 2;
if (true) {
    let a = 5;
    alert(`in the if block ${a}`);
}
alert(`outside of the if block ${a}`);

// a in if = 5
// a outside of if = 2

// #5.1 - run the code in the console
// #5.2 What will happen if the variable is declared with const instead of let ?
//still works

// 🌟 Exercise 2 : Ternary Operator

function winBattle(){
    return true;
}

const winBattle = () => true;

const experiencePoints = winBattle() ? 10 : 1;

console.log(experiencePoints);

// 🌟 Exercise 3 : Is It A String ?

const isString = (string) => typeof string === 'string' ? 'true' : 'false';

console.log(isString('hello'));
console.log(isString([1, 2, 4, 0]));

// 🌟 Exercise 4 : Find The Sum

const sum = (a, b) => a+b;

console.log(sum(2,5));

// 🌟 Exercise 5 : Kg And Grams

function convertToGrams (kg) {
    return kg * 1000
}

console.log(convertToGrams(8));

const convertToGramsAgain = function (kg) {
    return kg * 1000;
}

console.log(convertToGramsAgain(6));

// function declaration can be called upon before and after the function has been declared.
// function expressions are placed ina a varable and therefor cannot be called upon before the function is declared.

const convertToGramsOnceMore = (kg) => kg*1000;

console.log(convertToGramsOnceMore(4));

// 🌟 Exercise 6 : Fortune Teller

(function (numChildren, partnersName, location, job) {
  const divElement = document.createElement("div");
  const text = `You will be a ${job} in ${location}, and married to ${partnersName} with ${numChildren} kids.`;
  const divText = document.createTextNode(text);
  divElement.appendChild(divText);
  document.body.appendChild(divElement);
})("3", "someone", "Israel", "full stack developer");

// 🌟 Exercise 7 : Welcome

(function(username) {
    const navElement = document.querySelector('nav');
    const divElement = document.createElement('div');
    const imageElement = document.createElement('img');
    const profilePictureUrl = 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NXx8cHJvZmlsZSUyMHBpY3R1cmV8ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&w=700&q=60';

    imageElement.src = profilePictureUrl;
    imageElement.style.height= '50px';
    divElement.appendChild(imageElement);

    const divText = document.createTextNode(username);
    divElement.appendChild(divText);

    navElement.appendChild(divElement);
}('John'))

// 🌟 Exercise 8 : Juice Bar

// Part I
function makeJuice(size) {
  function addIngredients(ingredient1, ingredient2, ingredient3) {
    const divElement = document.createElement("div");
    const text = `The client wants a ${size} juice, containing ${ingredient1}, ${ingredient2}, and ${ingredient3}.`;
    const divText = document.createTextNode(text);
    divElement.appendChild(divText);
    document.body.appendChild(divElement);
  }
  addIngredients("apples", "oranges", "strawberries");
}
makeJuice("small");

// Part II
function makeJuice(size) {
  const ingredients = [];

  function addIngredients(ingredient1, ingredient2, ingredient3) {
    ingredients.push(ingredient1, ingredient2, ingredient3);
  }

  function displayJuice() {
    const divElement = document.createElement("div");
    let text = `The client wants a ${size} juice containing`;

    for (let item of ingredients) {
        text += ` ${item}`;
    }

    const divText = document.createTextNode(text);
    divElement.appendChild(divText);
    document.body.appendChild(divElement);
  }
  addIngredients("apples", "oranges", "strawberries");
  addIngredients("kiwis", "blueberries", "blackberries");
  displayJuice();
}
makeJuice("small");
