const inventory = [
  { id: 1, car_make: "Lincoln", car_model: "Navigator", car_year: 2009 },
  { id: 2, car_make: "Mazda", car_model: "Miata MX-5", car_year: 2001 },
  { id: 3, car_make: "Honda", car_model: "Accord", car_year: 1983 },
  {
    id: 4,
    car_make: "Land Rover",
    car_model: "Defender Ice Edition",
    car_year: 2010,
  },
  { id: 5, car_make: "Honda", car_model: "Accord", car_year: 1995 },
];

function getCarHonda(carInventory) {
  const firstHonda = carInventory.find((car) => car["car_make"] === "Honda");
  console.log(firstHonda);
  return `This is a ${firstHonda["car_make"]} ${firstHonda["car_model"]} from ${firstHonda["car_year"]}`;
}

console.log(getCarHonda(inventory));

// Decided to use a different kind of function
const sortCarInventoryByYear = (carInventory) => {
  carInventory.sort((a, b) => (a["car_year"] > b["car_year"] ? 1 : -1));
  return carInventory;
};

console.log(sortCarInventoryByYear(inventory));
