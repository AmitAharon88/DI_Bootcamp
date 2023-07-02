// 🌟 Exercise 1 : HTML Form

// 1-2:

//     <form method='GET'>
//         <label for='name'>Name</label><br>
//         <input id='name' type='text' name='Name'><br><br>
//         <label for='comments'>Comments</label><br>
//         <textarea name='textarea' id='comments' rows='5' cols='50'>Write your comment here</textarea><br><br>
//         <button type='submit'>Submit</button>
//     </form>

// 3. Form submission values are passed as part of the URL. Because i didnt specify an action the data will be sent to the URL of the page.



// 🌟 Exercise 2 : HTML Form #2
// 1-2.
// The form in the HTML will look like this:

//     <form method='POST'>
//         <label for='name'>Name</label><br>
//         <input id='name' type='text' name='Name'><br><br>
//         <label for='comments'>Comments</label><br>
//         <textarea name='textarea' id='comments' rows='5' cols='50'>Write your comment here</textarea><br><br>
//         <button type='submit'>Submit</button>
//     </form>

// 3. For submission values are sent to the server as part of the data body and will not be visible in the URL box in the user’s browser.





// 🌟 Exercise 3 : JSON Mario

const marioGame = {
    detail : "An amazing game!",
    characters : {
        mario : {
          description:"Small and jumpy. Likes princesses.",
          height: 10,
          weight: 3,
          speed: 12,
        },
        bowser : {
          description: "Big and green, Hates princesses.",
          height: 16,
          weight: 6,
          speed: 4,
        },
        princessPeach : {
          description: "Beautiful princess.",
          height: 12,
          weight: 2,
          speed: 2,
        }
    },
  }

const marioData = JSON.stringify(marioGame);
console.log(marioData);

// The nested objects are converted to JSON format along with their properties.

const gameData = JSON.stringify(marioGame, null, 2);
console.log(gameData);