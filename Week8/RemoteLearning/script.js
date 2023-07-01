// Question 1

function answer(array) {
  array.sort((a, b) => (a > b ? 1 : -1));
  console.log(array);

  const result = [];
  let currentArray = [];

  for (let i = 0; i < array.length; i++) {
    if (array[i] === array[i + 1]) {
      currentArray.push(array[i]);
    } else if (currentArray.length > 0) {
      currentArray.push(array[i]);
      result.push(currentArray);
      currentArray = [];
    } else {
      result.push(array[i]);
    }
  }
  return result;
}

console.log(answer([1, 2, 4, 591, 392, 391, 2, 5, 591, 10, 2, 1, 1, 1, 20, 20]));


// Question 2

function answerTwo ();

// answerTwo([1,2,3], 4) should return [1,3]