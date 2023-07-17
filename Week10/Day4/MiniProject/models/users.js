import { db } from "../config/db";

export const register = ({
    first_name,
    last_name,
    email,
    username,
    created_date,
    last_login_date,
    hash
}) => {
    db.transaction((trx) => {
        trx('users').insert ({
            first_name,
            last_name,
            email,
            username,
            created_date,
            last_login_date
        })
        .returning(['user_id', 'firstName', 'lastName', 'email', 'username'])
        .then(row => {
            return trx('login')
            .insert({
                username : row[0].username || username,
                password : hash
            })
            .then(row => {
                trx.commit;
            })
            .catch(err => {
                trx.rollback;
            })
        })
        .then(row => {
            trx.commit;
        })
        .catch(err => {
            trx.rollback;
        })
    });
};