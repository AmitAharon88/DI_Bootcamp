import './Exercise3.css';

const style_header = {
    color: "white",
    backgroundColor: "DodgerBlue",
    padding: "10px",
    fontFamily: "Arial"
  };

const Exercise = () => {
    return (
       <>
        <h1 style={style_header}>This is a Header</h1>
        <p className='para'>This is a paragraph</p>
        <a href='#'>This is a link</a>
        <form>
            <label for='form'>Enter your name:</label>
            <input  id='form' type='text' name='name'/>
            <button type="submit">Submit</button>
        </form>
        <img src='https://media3.giphy.com/media/Dh5q0sShxgp13DwrvG/200w.webp?cid=ecf05e4703q0a0qzcqd1kyrepz720wsgjcr00n940kkfbuqc&ep=v1_gifs_search&rid=200w.webp&ct=g' alt='coding gif'></img>
        <p>My list</p>
        <ul>
            <li>Snow</li>
            <li>Rain</li>
            <li>Sunshine</li>
            <li>Hail</li>
        </ul>
       </>
    );
};
    
    
export default Exercise;