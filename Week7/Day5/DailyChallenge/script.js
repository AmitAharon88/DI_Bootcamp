function SingSong() {
  let bottles = parseInt(prompt("Enter a number: "));
  let takeDown = 0;

  while (isNaN(bottles) || bottles <= 0) {
    bottles = parseInt(prompt("Invalid input. Enter a number > 0: "));
  }

  while (bottles > 0) {
    console.log(`${bottles} bottles of beer on the wall`);
    console.log(`${bottles} bottles of beer`);
    takeDown += 1;
    bottles -= takeDown;
    if (takeDown === 1) {
      console.log(`Take ${takeDown} down, pass it around`);
      console.log(`${bottles} bottles of beer on the wall\n`);
    } else if (bottles > takeDown) {
      console.log(`Take ${takeDown} down, pass them around`);
      console.log(`${bottles} bottles of beer on the wall\n`);
    } else {
      console.log(`Take ${bottles} down, pass them around`);
      console.log(`${bottles} bottles of beer on the wall\n`);
    }
  }
}

SingSong();
