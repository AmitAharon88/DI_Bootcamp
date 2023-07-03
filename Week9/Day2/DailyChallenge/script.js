// 1st Daily Challenge

function makeAllCaps(array) {
  const promise1 = new Promise((resolve, reject) => {
    if (array.every((word) => typeof word === "string")) {
      resolve(array.join(" ").toUpperCase().split(" "));
    } else {
      reject("Not all the words in the array are strings.");
    }
  });
  return promise1;
}

function sortWords(array) {
  const promise2 = new Promise((resolve, reject) => {
    if (array.length > 4) {
      resolve(array.sort());
    } else {
      reject("Array length to short");
    }
  });
  return promise2;
}

//in this example, the catch method is executed
makeAllCaps([1, "pear", "banana"])
  .then((arr) => sortWords(arr))
  .then((result) => console.log(result))
  .catch((error) => console.log(error));

//in this example, the catch method is executed
makeAllCaps(["apple", "pear", "banana"])
  .then((arr) => sortWords(arr))
  .then((result) => console.log(result))
  .catch((error) => console.log(error));

//in this example, you should see in the console,
// the array of words uppercased and sorted
makeAllCaps(["apple", "pear", "banana", "melon", "kiwi"])
  .then((arr) => sortWords(arr))
  .then((result) => console.log(result)) //["APPLE","BANANA", "KIWI", "MELON", "PEAR"]
  .catch((error) => console.log(error));

// 2nd Daily Challenge

const morse = `{
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-"
}`;

function toJs() {
  const jsObj = JSON.parse(morse);
  const promise = new Promise((resolve, reject) => {
    if (Object.values(jsObj).length === 0) {
      reject("Error: Empty object");
    } else {
      resolve(jsObj);
    }
  });
  return promise;
}

function toMorse(morseJS) {
  const userInput = prompt("Provide a word or sentence: ");
  const userArray = userInput
    .split(" ")
    .join("")
    .toLowerCase()
    .split("");

  const promise2 = new Promise((resolve, reject) => {
    if (
      userArray.every((element) => Object.keys(morseJS).includes(element))
    ) {
      const morseArray = userArray.map((element) => morseJS[element]);
      resolve(morseArray);
    } else {
      reject("Error: Invalid characters");
    }
  });
  return promise2;
}

function joinWords(morseTranslation) {
    for (let element of morseTranslation) {
        const pElement = document.createElement('p');
        const pText = document.createTextNode(element);
        pElement.appendChild(pText);
        document.body.appendChild(pElement);
    }
}

// Can also write the function like this but for some reason the '\n' is not providing a new line for me.
// function joinWords(morseTranslation) {
//     const pElement = document.createElement('p');
//     const pText = document.createTextNode(morseTranslation.join('\n'));
//     pElement.appendChild(pText);
//     document.body.appendChild(pElement);
// }


toJs()
  .then((result) => toMorse(result))
  .then((result) => joinWords(result))
  .catch((error) => console.log(error));
