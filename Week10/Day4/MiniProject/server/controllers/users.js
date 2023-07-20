import { registerUser, checkForUser } from "../models/users.js";
import bcrypt from "bcrypt";


export const _registerUser = async (req, res) => {
    console.log("req", req.body)
    const first_name = req.body.fname;
    const last_name = req.body.lname;
    const username = req.body.username.toLowerCase();
    const email = req.body.email.toLowerCase();
    const password = req.body.password + "";

    const salt = bcrypt.genSaltSync(10);
    const hash = bcrypt.hashSync(password, salt);

    try {
        const newUser = await registerUser({
            first_name,
            last_name,
            username,
            email,
            hash
            }
        );
        console.log(newUser)
        res.status(200).json({message: `Hello ${first_name} ${last_name}. Your ID is: ${newUser[0].user_id}`})
    } catch (e) {
        // console.log(e)
        res.status(400).json({error: `${email} already exists`});
    };
};

export const _checkForUser = async (req, res) => {
    const username = req.body.username.toLowerCase();
    const password = req.body.password + "";
    try {
        const userCheck = await checkForUser(username)
        console.log(userCheck)
        if (userCheck.length === 0) {
            res.status(400).json({error: `Username or password does not exist.`})
        } else {
            const match = bcrypt.compareSync(password, userCheck[0].password);
            if (match) {
                res.status(200).json({message: `Hello, your username is ${username}`})
            } else {
                res.status(400).json({error: `Password incorrect`})
            }
        }
    } catch(e) {
        console.log(e);
        res.status(500).json({error: "Internal server error"});
    };
};