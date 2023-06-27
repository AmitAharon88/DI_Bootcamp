const gameInfo = [
    {
      username: "john",
      team: "red",
      score: 5,
      items: ["ball", "book", "pen"]
    },
    {
      username: "becky",
      team: "blue",
      score: 10,
      items: ["tape", "backpack", "pen"]
    },
    {
      username: "susy",
      team: "red",
      score: 55,
      items: ["ball", "eraser", "pen"]
    },
    {
      username: "tyson",
      team: "green",
      score: 1,
      items: ["book", "pen"]
    },
   ];

const usernames = [];
gameInfo.forEach((element) => usernames.push(`${element['username']}!`));
console.log(usernames);

const winners = []
gameInfo.forEach((element) => element['score'] > 5 ? winners.push(`${element['username']}`) : null )
console.log(winners);

// Not sure if there is a shorter way of doing this.
const allScores = []
gameInfo.forEach((element) => allScores.push(element['score']))
const totalScore = allScores.reduce((acc, userScore) => acc + userScore)
console.log(totalScore);