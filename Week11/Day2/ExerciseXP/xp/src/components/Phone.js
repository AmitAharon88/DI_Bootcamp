import { useState } from 'react';

const Phone = () => {
  const [phoneInfo, setPhoneInfo] = useState({
    brand: "Samsung",
    model: "Galaxy S20",
    color: "black",
    year: 2020
  });

  const changeColor = () => {
    setPhoneInfo(prevPhoneInfo => ({
        ...prevPhoneInfo,
        color: "blue"
    }));
  };


  return (
    <>
        <h3>My phone is a {phoneInfo.brand}</h3>
        <p>It is a {phoneInfo.color} {phoneInfo.model} from {phoneInfo.year}</p>
        <button onClick={changeColor}>Change color</button>

    </>
  )
};

export default Phone