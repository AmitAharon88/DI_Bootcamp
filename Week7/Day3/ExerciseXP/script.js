// Exercise 1

const people = ["Greg", "Mary", "Devon", "James"];

// Part I
// 1.
people.splice(0, 1);
console.log(people);

// 2.
people.splice(2, 1, "James");
console.log(people);

// 3.
people.push("Amit");
console.log(people);

// 4.
const maryIndex = people.indexOf("Mary");
console.log(maryIndex);

// 5.
const peopleCopy = people.slice(1, people.length - 1);
console.log(peopleCopy);

// 6.
const FooIndex = people.indexOf("Foo");
console.log(FooIndex);
// it returns -1 because it doesn't exist in the array.

// 7.
const last = people[people.length - 1];
console.log(last);
// With the array ['Mary', 'Devon', 'James', 'Amit'], the index of the last element is 3. The length of the element is 4.

// Part II
// 1. Here is 3 ways to do it
for (let person of people) {
  console.log(person);
}

for (index = 0; index < people.length; index++) {
  console.log(people[index]);
}

for (let index in people) {
  console.log(people[index]);
}

// 2.
for (index = 0; index < people.length; index++) {
  console.log(people[index]);

  if (people[index] === "Devon") {
    break;
  }
}

// Exercise 2

// 1.
const colors = ["blue", "red", "green", "black", "white"];

// 2.
for (let index = 0; index < colors.length; index++) {
  const sentence = `My #${index + 1} is ${colors[index]}`;
  console.log(sentence);
}

// 3.
const suffixes = ["1st", "2nd", "3rd", "4th", "5th"];

for (let index = 0; index < colors.length; index++) {
    const color = colors[index];
    const suffix = suffixes[index];
    const sentence = `My #${suffix} choice is ${color}`;
    console.log(sentence);
  }

// Exercise 3

// 1
const userInput = prompt('Provide a number: ');
console.log(typeof userInput);

// 2.
let number = parseFloat(userInput);

while (number <10) {
    const userInput = prompt('Provide a number: ');
    number = parseFloat(userInput);
}

console.log("Number greater than or equal to 10 entered:", number);

// Exercise 4

//  1.
const building = {
  numberOfFloors: 4,
  numberOfAptByFloor: {
    firstFloor: 3,
    secondFloor: 4,
    thirdFloor: 9,
    fourthFloor: 2,
  },
  nameOfTenants: ["Sarah", "Dan", "David"],
  numberOfRoomsAndRent: {
    sarah: [3, 990],
    dan: [4, 1000],
    david: [1, 500],
  },
};

// 2.
const numFloors = building["numberOfFloors"];
console.log(numFloors);

// 3.
const numApt = building["numberOfAptByFloor"];
console.log(numApt["firstFloor"]);
console.log(numApt["thirdFloor"]);

// 4.
const tenants = building["nameOfTenants"];
console.log(tenants[2]);
const tenantsApt = building["numberOfRoomsAndRent"];
console.log(tenantsApt['dan'][0]);

// 5.
const sarahsRent = tenantsApt['sarah'][2];
const davidsRent = tenantsApt['david'][2];
const dansRent = tenantsApt['dan'][2];

if (sarahsRent + davidsRent < dansRent) {
    dansRent += 1200
    console.log('Dan got a raise')
} else {
    console.log('No Raises')
  }


// Exercise 5

// 1.
const family = {
  firstName: ['Shula', 'Rahamim', 'Gilat', 'Kfir', 'Amit'],
  lastName: 'Aharon',
  amount: 5
}

// 2.
for (let key in family){
	console.log(key);
}

// 3.
for (let value in family) {
    console.log(family[value]);
}


// Exercise 6

const details = {
    my: 'name',
    is: 'Rudolf',
    the: 'raindeer'
  }

let sentence = '';
for (let key in details) {
    sentence += `${key} ${details[key]} `;
}
console.log(sentence);


// Exercise 7
const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
names.sort()
let secretSociety = ''
for (let name of names ) {
    secretSociety += (name[0])
}
console.log(secretSociety)