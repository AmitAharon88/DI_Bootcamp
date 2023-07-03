// Exercise 1 : Promise.All()

const promise1 = Promise.resolve(3);

const promise2 = 42;

const promise3 = new Promise((resolve, reject) => {
  setTimeout(resolve, 3000, "foo");
});

Promise.all([promise1, promise2, promise3]).then(
  ((result) => console.log(result)).catch((error) => console.log("ERROR"))
);

// Promise.all works by accepting an iterable (array or string) adding .then() and .catch(). We receive all the resolves in an array because none were rejected.

// Exercise 2 : Analyse Promise.All()

function timesTwoAsync(x) {
  return new Promise((resolve) => resolve(x * 2));
}

const arr = [1, 2, 3];
const promiseArr = arr.map(timesTwoAsync);

Promise.all(promiseArr).then((result) => {
  console.log(result);
});

// the outcome will be an array of the arr array multiplied by 2
