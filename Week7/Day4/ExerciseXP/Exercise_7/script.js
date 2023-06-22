const books = [
  {
    title: "Harry Potter",
    author: "J.K. Rowling",
    image: "https://m.media-amazon.com/images/I/71-++hbbERL.jpg",
    alreadyRead: true,
  },
  {
    title: "To Kill a Mocking Bird",
    author: "Harper Lee",
    image:
      "https://media.glamour.com/photos/56e1f3c4bebf143c52613c04/master/w_1600,c_limit/entertainment-2016-02-12-main.jpg",
    alreadyRead: false,
  },
];

for (const book of books) {
  const bookDiv = document.createElement("div");
  const image = document.createElement("img");
  image.src = book["image"];
  const text = document.createTextNode(
    `${book["title"]} written by ${book["author"]}`
  );
  bookDiv.appendChild(text);
  bookDiv.appendChild(image);
  document.body.appendChild(bookDiv);

  image.style.width = "100px";

  if (book["alreadyRead"] === true) {
    bookDiv.style.color = "red";
  }
}
