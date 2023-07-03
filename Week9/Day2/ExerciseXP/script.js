// 🌟 Exercise 1 : Comparison

function compareToTen(num) {
    const promise = new Promise ((reslove, reject) => {
        if (num <= 10){
            reslove('This is a low number');
        } else {
            reject('This is a high number');
        }
    });
    return promise
}

//In the example, the promise should reject
compareToTen(15)
  .then(result => console.log(result))
  .catch(error => console.log(error));

//In the example, the promise should resolve
compareToTen(8)
  .then(result => console.log(result))
  .catch(error => console.log(error));


//   🌟 Exercise 2 : Promises

const promise2 = new Promise ((resolve) => {
    setTimeout(() => {
        resolve("success")
    }, 4000)
});

promise2.then(result => console.log(result));


// 🌟 Exercise 3 : Resolve & Reject
const promise3a = new Promise(resolve => resolve(3));
const promise3b = Promise.resolve(3);
const promise4a = new Promise(reject => reject('Boo!'));
const promise4b = Promise.resolve('Boo!');