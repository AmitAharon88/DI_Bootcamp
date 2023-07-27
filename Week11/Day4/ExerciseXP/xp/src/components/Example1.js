import React from 'react';
import jsonData from '../data-ex1.json'

console.log(jsonData)

class Example1 extends React.Component {
    constructor() {
        super();
        //define the state object
        this.state ={
            data: []
        };
    };

    componentDidMount () {
        console.log(jsonData.SocialMedias)
        this.setState({ data: jsonData.SocialMedias });
    };

    render() {
        return(
            <>
                <h2>Social Media Links</h2>
                <ul>
                    {
                        this.state.data.map(item => {
                            return (
                                <li key={item}>
                                    <a href={item}>{item}</a>
                                </li>
                            )
                        })
                    }
                </ul>
            </>
        )
    };
};
      
export default Example1;