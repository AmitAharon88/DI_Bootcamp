import express from "express";
import cors from "cors";
// import router from "./routes/router.js";

const app = express();

app.use(cors());
app.use(express.urlencoded({ extended: true }));
app.use(express.json());

// app.use('userRouter');

app.listen("3000", () => {
    console.log("SERVER LISTENING");
});
