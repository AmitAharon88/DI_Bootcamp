function singSong() {
  let bottles = parseInt(prompt("Enter a number: "));
  let takeDown = 0;

  while (isNaN(bottles) || bottles <= 0) {
    bottles = parseInt(prompt("Invalid input. Enter a number > 0: "));
  }
  while (bottles > takeDown) {
    console.log(`${bottles} bottles of beer on the wall`);
    console.log(`${bottles} bottles of beer`);
    takeDown += 1;
    bottles -= takeDown;
    if (takeDown === 1) {
      console.log(`Take ${takeDown} down, pass it around`);
      console.log(`${bottles} bottles of beer on the wall\n`);
    } else {
      console.log(`Take ${takeDown} down, pass them around`);
      console.log(`${bottles} bottles of beer on the wall\n`);
    }
  }
  console.log(`${bottles} bottles of beer on the wall`);
  console.log(`${bottles} bottles of beer`);
  console.log(`Take ${bottles} down, pass them around`);
  bottles -= bottles;
  console.log(`${bottles} bottles of beer on the wall\n`);
}
singSong();

// Another way to write it (from class)
// function generateBeerSong(numBottles) {
//   for (let i = 1; numBottles > 0; i >= numBottles ? i = numBottles : i++) {
//       console.log(`${numBottles} bottle${numBottles !== 1 ? 's' : ''} of beer on the wall`);
//       console.log(`${numBottles} bottle${numBottles !== 1 ? 's' : ''} of beer`);
//       console.log(`Take ${i} down, pass ${i === 1 ? 'it' : 'them'} around`);
//       numBottles = numBottles - i;
//       if (numBottles >= 1) {
//           console.log(`${numBottles} bottle${numBottles !== 1 ? 's' : ''} of beer on the wall\n`);
//       } else {
//           console.log(`No more bottles of beer on the wall\n`);
//       }
//   }
// }

// let numBottles = parseInt(prompt('Enter the number of bottles to start the song:'));
// generateBeerSong(numBottles);
