import express from "express";
import dotenv from "dotenv";
import cors from "cors";

// import { fileURLToPath } from 'url';
// import { dirname } from 'path';
// import { createUser } from "../models/register.js";

const app = express();
app.use(cors());
// for creating a new user- register- coming from body parser
app.use(express.urlencoded({ extended: true }));
app.use(express.json());

dotenv.config();


// const __filename = fileURLToPath(import.meta.url);
// const __dirname = dirname(__filename);

// app.use("/", express.static(__dirname + "/public")); 

// app.get('/', (req, res) => {
//     res.sendFile(__dirname+'/public/index.html')
// })

app.listen(process.env.PORT || 3001, () => {
    console.log(`run on port ${process.env.PORT || 3001}`);
});

// BELOW NOT SURE IF RIGHT

// created new user- register
// app.post('/', (req, res) => {
//     try {
//         const hashedPassword = await bcrypt.hash(req.body.password, 10)
//         createUser ({
//             firstName: req.body.firstName,
//             lastName: req.body.lastName,
//             email: req.body.email,
//             username: req.body.username,
//             password: hashedPassword,
//         })
//         res
//     }
// })

