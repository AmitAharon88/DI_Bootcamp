import db from "../config/db.js";

export const registerUser = async ({first_name, last_name, email, username, hash}) => {
    const trx = await db.transaction();
    try {
        const newUser = await db("register")
        .insert({
            first_name,
            last_name,
            email,
            username,
            last_login: new Date()
            },
            ["user_id", "first_name", "last_name", "email", "username"]
        )
        .transacting(trx);
        console.log("user", newUser)

        const login = await db("login")
        .insert({
            username: username,
            password: hash
            },
            ["login_id", "username", "password"]
        )
        .transacting(trx);
        console.log("login", login)

        await trx.commit();
        return newUser;     // returning a promise
    } catch (err) {
        await trx.rollback();
        throw new Error (err.message);
    };
};

// use for login button

export const checkForUser = async (username) => {
    const answer = await db("login").where("username", username).select("password");
    return answer
};