import React from 'react';

class Child extends React.Component {
    componentWillUnmount() {
      alert("Unmounted: Child component is being removed from the DOM.");
    };
  
    render () {
      if (!this.props.show) {
        return null;
      } else{
        return (
          <>
              <header>"Hello"</header>
              <button onClick={this.props.changeShow}>Delete</button>
          </>
        )
      }
    };
};

export default Child