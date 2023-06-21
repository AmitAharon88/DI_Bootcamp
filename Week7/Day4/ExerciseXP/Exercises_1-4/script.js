// 🌟 Exercise 1 : Find The Numbers Divisible By 23
let numSum = 0;
function displayNumbersDivisible() {
  for (let num = 0; num < 501; num++) {
    if (num % 23 === 0) {
      console.log(num);
      numSum += num;
    } else {
      continue;
    }
  }
  console.log(numSum);
}

displayNumbersDivisible();

// BONUS
let numSum2 = 0;
function displayNumbersDivisible2(divisor) {
  for (let num = 0; num < 501; num++) {
    if (num % divisor === 0) {
      console.log(num);
      numSum += num;
    } else {
      continue;
    }
  }
  console.log(numSum);
}

displayNumbersDivisible2(65);

// 🌟 Exercise 2 : Shopping List

const stock = {
  banana: 6,
  apple: 0,
  pear: 12,
  orange: 32,
  blueberry: 1,
};

const prices = {
  banana: 4,
  apple: 2,
  pear: 1,
  orange: 1.5,
  blueberry: 10,
};

const shoppingList = {
  banana: 1,
  apple: 1,
  orange: 1,
};

let totalCost = 0;

function myBill() {
  for (let item in shoppingList) {
    if (stock[item] > shoppingList[item]) {
      totalCost += prices[item];
      stock[item] -= shoppingList[item];
    }
  }
  console.log(totalCost);
}

myBill();

// Exercise 3 : What’s In My Wallet ?
const quarter = 0.25;
const dime = 0.1;
const nickel = 0.05;
const penny = 0.01;

function changeEnough(itemPrice, amountOfChange) {
  const totalChange =
    amountOfChange[0] * quarter +
    amountOfChange[1] * dime +
    amountOfChange[2] * nickel +
    amountOfChange[3] * penny;
  const action = itemPrice <= totalChange ? true : false;
  return action;
}

console.log(changeEnough(4.25, [25, 20, 5, 0]));

// 🌟 Exercise 4 : Vacations Costs

// 1,
function hotelCost() {
  const userInput = prompt(
    "How many nights would you like to stay at the hotel? "
  );
  while (userInput === null || isNaN(userInput)) {
    userInput = prompt(
      "Please enter a valid number for the number of nights for your stay: "
    );
  }
  const numberOFNights = userInput;
  return numberOFNights * 140;
}

console.log(hotelCost());

// 2.

const destinations = {
  London: 183,
  Paris: 220,
  "All other destination": 300,
};

function planeRideCost() {
  const userInput = prompt("What is your destination? ");
  while (userInput === null || typeof userInput !== "string") {
    userInput = prompt("Please enter a valid destination: ");
  }
  for (const destination in destinations) {
    if (destination === userInput) {
      return destinations[destination];
    } else {
      return destinations["All other destination"];
    }
  }
}

console.log(planeRideCost());

// 3.

function rentalCarCost() {
  const userInput = prompt("How many days would you like to rent a car? ");
  while (userInput === null || isNaN(userInput)) {
    userInput = prompt(
      "Please enter the number of days you would like to rent a car: "
    );
  }
  if (userInput > 10) {
    const totalCost = userInput * 40;
    const discountCost = totalCost * 0.05;
    const finalCost = totalCost - discountCost;
    return finalCost;
  } else {
    return userInput * 40;
  }
}

console.log(rentalCarCost());

// 4.

function totalVacationCost() {
  const costOfHotel = hotelCost();
  const costOfPlane = planeRideCost();
  const costOfCar = rentalCarCost();
  const totalCost = costOfHotel + costOfPlane + costOfCar;
  return `Your total vacation cost is $${totalCost}: $${costOfHotel} for a hotel, $${costOfPlane} for a flight, $${costOfCar} for a car`;
}

console.log(totalVacationCost());
