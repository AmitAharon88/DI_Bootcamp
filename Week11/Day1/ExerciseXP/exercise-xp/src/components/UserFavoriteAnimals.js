const UserFavoriteAnimals = ({favAnimals}) => {
    return (
       <>
        <ul>
            {favAnimals.map((animal) => 
                <li key={animal}>{animal}</li>
            )}
        </ul>
       </>
    );
};
    
    
export default UserFavoriteAnimals;
    