import ErrorBoundary from './components/ErrorBoundary';
import Home from './components/HomeScreen';
import Profile from './components/ProfileScreen';
import Shop from './components/ShopScreen';
import PostList from './components/PostList';
import Example1 from './components/Example1';
import Example2 from './components/Example2';
import Example3 from './components/Example3';
import { Routes, Route, NavLink } from "react-router-dom";
import "bootstrap/dist/css/bootstrap.min.css";
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import './App.css';

function App() {
  const obj = {
    key1: 'myusername',
    email: 'mymail@gmail.com',
    name: 'Isaac',
    lastname: 'Doe',
    age: 27
  };

  const fetchData = async () => {
    try {
        // snd data to the body of this url
        const res = await fetch("https://webhook.site/6eda0a5a-e4b8-44c4-a76f-417ed28caa2b", {
          method: "POST",
          headers: {"content-type":"application/json"},
          // convert obj to json
          body: JSON.stringify(obj)
        })
        console.log(res)
    } catch (e) {
        console.log(e);
    };
  };

  return (
    <div className="App">
      <header className="App-header">
        <Navbar bg="primary" data-bs-theme="dark">
          <Container>
            <Navbar.Brand >ExerciseXP</Navbar.Brand>
            <Nav className="me-auto">
              <NavLink to="/">Home</NavLink>{" "}
              <NavLink to="/profile">Profile</NavLink>{" "}
              <NavLink to="/shop">Shop</NavLink>{" "}
            </Nav>
          </Container>
        </Navbar>
        <Routes>
          <Route path="/" element={<ErrorBoundary><Home /></ErrorBoundary>}/>
          <Route path="/profile" element={<ErrorBoundary><Profile /></ErrorBoundary>}/>
          <Route path="/shop" element={<ErrorBoundary><Shop /></ErrorBoundary>}/>
        </Routes>
        <hr/>
        <PostList />
        <hr/>
        <Example1 />
        <hr/>
        <Example2 />
        <hr/>
        <Example3 />
        <hr/>
        <button onClick={fetchData}>Display Data</button>
      </header>
    </div>
  );
}

export default App;
