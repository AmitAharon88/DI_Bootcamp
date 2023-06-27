// 🌟 Exercise 1 : Colors

const colors = ["Blue", "Green", "Red", "Orange", "Violet", "Indigo", "Yellow"];

const favColors = colors.map((color, i) => `${i+1}# choice is ${color}.`);
console.log(favColors);

const containsViotet = colors.some((color) => color === 'Viotet' ? console.log('Yeah') : console.log('No...'));

// 🌟 Exercise 2 : Colors #2
const colors2 = ["Blue", "Green", "Red", "Orange", "Violet", "Indigo", "Yellow"];
const ordinal = ["th","st","nd","rd"];

// Long way
const favColors2 = colors2.map((color, i) => {
    const colorNum = i + 1
    let prefix
    if (colorNum > 3 ) {
        prefix = `${colorNum}${ordinal[0]}`
    } else if (colorNum === 1) {
        prefix = `${colorNum}${ordinal[1]}`
    } else if (colorNum === 2) {
        prefix = `${colorNum}${ordinal[2]}`
    } else {
        prefix = `${colorNum}${ordinal[3]}`
    }
    return `${prefix} choice is ${color}.`;
})

console.log(favColors2);

// Short way
const favColors3 = colors2.map((color, index) => {
  const colorNumber = index + 1;
  const ordinalSuffix =
    colorNumber > 3 ? ordinal[0] : ordinal[colorNumber];
  return `${colorNumber}${ordinalSuffix} choice is ${color}.`;
});

console.log(favColors3);

// Exercise 3 : Analyzing
// ------1------
const fruits = ["apple", "orange"];
const vegetables = ["carrot", "potato"];

const result = ['bread', ...vegetables, 'chicken', ...fruits];
console.log(result);

// output --> ['bread', "carrot", "potato", 'chicken', "apple", "orange"]

// ------2------
const country = "USA";
console.log([...country]);

// output --> ["U", "S", "A"]

// ------Bonus------
let newArray = [...[,,]];
console.log(newArray);

// output --> [undefined, undefined]

// 🌟 Exercise 4 : Employees

const users = [{ firstName: 'Bradley', lastName: 'Bouley', role: 'Full Stack Resident' },
             { firstName: 'Chloe', lastName: 'Alnaji', role: 'Full Stack Resident' },
             { firstName: 'Jonathan', lastName: 'Baughn', role: 'Enterprise Instructor' },
             { firstName: 'Michael', lastName: 'Herman', role: 'Lead Instructor' },
             { firstName: 'Robert', lastName: 'Hajek', role: 'Full Stack Resident' },
             { firstName: 'Wes', lastName: 'Reid', role: 'Instructor'},
             { firstName: 'Zach', lastName: 'Klabunde', role: 'Instructor'}];

const welcomeStudents = users.map((element) => `Hello ${element['firstName']}`);

console.log(welcomeStudents);

const fullStackStudents = users.filter((element) => element['role'] === 'Full Stack Resident')

console.log(fullStackStudents);

const fullStackStudentsName = users
.filter((element) => element['role'] === 'Full Stack Resident')
.map((element) => element['lastName']);

console.log(fullStackStudentsName);

// 🌟 Exercise 5 : Star Wars

const epic = ['a', 'long', 'time', 'ago', 'in a', 'galaxy', 'far far', 'away'];

const epicString = epic.reduce((acc, currentWord) => `${acc} ${currentWord}`);
console.log(epicString);

// 🌟 Exercise 6 : Employees #2

const students = [
  { name: "Ray", course: "Computer Science", isPassed: true },
  { name: "Liam", course: "Computer Science", isPassed: false },
  { name: "Jenner", course: "Information Technology", isPassed: true },
  { name: "Marco", course: "Robotics", isPassed: true },
  { name: "Kimberly", course: "Artificial Intelligence", isPassed: false },
  { name: "Jamie", course: "Big Data", isPassed: false },
];

const passedStudents = students.filter(
  (element) => element["isPassed"] === true
);
console.log(passedStudents);

const passedStudents2 = students
  .filter((element) => element["isPassed"] === true)
  .forEach(
    (element) => console.log(`Good job ${element["name"]}, you passed the course in ${element['course']}`)
  );