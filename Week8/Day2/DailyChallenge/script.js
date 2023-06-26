let client = "John";

const groceries = {
  fruits: ["pear", "apple", "banana"],
  vegetables: ["tomatoes", "cucumber", "salad"],
  totalPrice: "20$",
  other: {
    payed: true,
    meansOfPayment: ["cash", "creditCard"],
  },
};

const displayGroceries = () => {
    groceries["fruits"].forEach((fruit) => {
        console.log(fruit);
    });
};

const cloneGroceries = () => {
    let user = client;    // user='John'--> same value as client but they are 2 different variables.
    user = 'Betty';       // Wont change the other one when changed.
    console.log(user, client);

    const shopping = groceries;
    shopping["totalPrice"] = '$35'; // Yes because its an object. Not recating a copy just creating a new refernce.
    shopping["other"]['payed'] = false; // Yes because its an object. Not recating a copy just creating a new refernce.
    console.log('shopping:', shopping);
    console.log('groceries:', groceries);
}

displayGroceries();
cloneGroceries();
