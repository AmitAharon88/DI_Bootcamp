// function PlayTheGame() {
//   const play = confirm("Would you like to play?");

//   if (!play) {
//     alert("No problem, Goodbye");
//   } else {
//     const userInput = parseInt(prompt("Enter and number between 0-10: "));

//     if (isNaN(userInput)) {
//       alert("Sorry not a number, Goodbye.");
//     } else if (userInput < 0 || userInput > 10) {
//       alert("Sorry its not a good number, Goodbye.");
//     } else {
//       const computerNumber = Math.round(Math.random() * 10);
//       compareNumbers(userInput, computerNumber);
//     }
//   }
// }

// function compareNumbers(userNumber, computerNumber) {
//   let attempts = 1;
//   while (attempts < 3) {
//     if (userNumber === computerNumber) {
//       alert("Winner");
//       return;
//     } else if (userNumber > computerNumber) {
//       userNumber = parseInt(
//         prompt("Your number is bigger then the computers, guess again")
//       );
//     } else {
//       userNumber = parseInt(
//         prompt("Your number is smaller then the computers, guess again")
//       );
//     }
//     attempts++;
//   }
//   alert("Out of chances");
//   return;
// }

// PlayTheGame();

// Mini Project with Bonus
function PlayTheGame() {
  const play = confirm("Would you like to play?");

  if (!play) {
    alert("No problem, Goodbye");
  } else {
    let userInput = parseInt(prompt("Enter and number between 0-10: "));

    while (isNaN(userInput)) {
      userInput = parseInt(
        prompt("Sorry not a number, Please enter a number: ")
      );
    }
    while (userInput < 0 || userInput > 10) {
      userInput = parseInt(
        prompt("Sorry its not a good number. Enter an number form 0-10: ")
      );
    }
    const computerNumber = Math.round(Math.random() * 10);
    compareNumbers(userInput, computerNumber);
  }
}

function compareNumbers(userNumber, computerNumber) {
  let attempts = 1;
  while (attempts < 3) {
    if (userNumber === computerNumber) {
      alert("Winner");
      return;
    } else if (userNumber > computerNumber) {
      userNumber = parseInt(
        prompt("Your number is bigger then the computers, guess again")
      );
    } else {
      userNumber = parseInt(
        prompt("Your number is smaller then the computers, guess again")
      );
    }
    attempts++;
  }
  alert("Out of chances");
  return;
}

PlayTheGame();
