import React from 'react';
import Child from './Child';

class Color extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      color: "red",
      timer: null,
      show: true
    };
  };

  componentDidMount() {
    this.timer = setTimeout(() => {
      this.setState({ color: "yellow" });
    }, 3000); // Change to the desired delay in milliseconds (3 seconds in this example)
  };

  shouldComponentUpdate(nextProps, nextState) {
    // Always return true, allowing the component to update and re-render.
    return true;
  };

  componentDidUpdate () {
    console.log("after update")
  };

  getSnapshotBeforeUpdate() {
    console.log("in getSnapshotBeforeUpdate");
    return null;
  };

  changeColorToBlue = () => {
    this.setState({color: "blue"});
  };

  changeShow = () => {
    this.setState({show: false});
  };

  render (props) {

    return (
      <>
          <header>My Favorite Color is <em>{this.state.color}</em></header>
          <button onClick={this.changeColorToBlue}>Change color</button>
          <Child show={this.state.show} changeShow={this.changeShow} />
      </>
    )
  };
};

// MOVED TO A DIFFERENT COMPONENT FILE
// class Child extends React.Component {
//   componentWillUnmount() {
//     alert("Unmounted: Child component is being removed from the DOM.");
//   };

//   render () {
//     if (!this.props.show) {
//       this.componentWillUnmount;
//       return null;
//     } else{
//       return (
//         <>
//             <header>"Hello"</header>
//             <button onClick={this.props.changeShow}>Delete</button>
//         </>
//       )
//     }
//   };


export default Color