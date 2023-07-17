const express = require('express');
const ejs = require('ejs');
const cors = require('cors');

const app = express();

app.set('view engine', 'ejs');

const Parser = require('rss-parser');
const parser = new Parser();


async function run () {
    const feed = await parser.parseURL('https://thefactfile.org/feed/');
    console.log(feed.title);
  
    feed.items.forEach(item => {
      console.log(item.title + ':' + item.link)
    }); 
};

run ();

// set the view engine to ejs
// sets EJS as the view engine for the Express application app.set('view engine', 'ejs');


app.get('/', (req, res) => {
    res.render('index', ) 	
    })
    

app.listen(process.env.PORT || 3001, ()=>{
    console.log('run on port 3001')
})


