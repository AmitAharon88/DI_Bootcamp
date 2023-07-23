import {promises as fsPromises} from "fs" ;

export const readuser = async (currentUser) => {
    console.log("in readuser");
    
    const data = await fsPromises.readFile("../data.json")
    .catch((err) => console.error('Failed to read file', err));
    
    const datausers = JSON.parse(data); //array of objects

    console.log("datausers", datausers);
    
    const findUser = datausers.findIndex((element) => 
            element.username === currentUser.username)

    console.log("findUser", findUser);

    if (findUser >= 0) {
        console.log("Username already exists");
        return "User already exists";
    } else {
        datausers.push(currentUser);
        console.log("User added successfully", datausers);
        //VERY IMPORTANT TO STRINGIFY THE DATA SENT TO WRITE FILES
        await fsPromises.writeFile(__dirname + "/public/data.json", JSON.stringify(datausers));
        return "Hello, Your account has been created";
    }
}
