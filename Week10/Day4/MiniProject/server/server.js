import express from "express";
import dotenv from "dotenv";
import cors from "cors";
import router from "./routes/routes.js"

dotenv.config();

const app = express();

app.use(cors());
// for creating a new user- register- coming from body parser
// app.use(express.urlencoded({ extended: true }));
app.use(express.json());
app.use(router);



app.listen(process.env.PORT || 3001, () => {
    console.log(`run on port ${process.env.PORT || 3001}`);
});

