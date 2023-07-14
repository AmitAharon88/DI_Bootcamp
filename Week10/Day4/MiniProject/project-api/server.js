import express from "express";
import dotenv from "dotenv";
import prouter from "./routes/page.js";
import path from 'path'
// import pageRouter from "./routes/page.js";


const app = express();
dotenv.config();

const __dirname = path.resolve()

// to create a POST- add data from form to db
// app.use(express.urlencoded({ extended: true }));
// app.use(express.json());

app.use("/", express.static(__dirname + "/public"));

app.use('/api/page',prouter);

app.listen(process.env.PORT, () => {
console.log(`run on port ${process.env.PORT}`);
});

app.use('/api/page',prouter);