import { useState, useEffect } from 'react';

const Color = () => {
  const [favColor, setFavColor] = useState("red");

  useEffect(() => {
    alert("useEffect reached");
  }, [favColor]);

  const changeColorToBlue = () => {
    setFavColor("blue");
  };

  return (
    <>
        <header>My Favorite Color is <em>{favColor}</em></header>
        <button onClick={changeColorToBlue}>Change color</button>
    </>

  )
};

export default Color