import React from 'react';
import jsonData from '../data-ex1.json'

class Example3 extends React.Component {

    render() {
        return(
            <>
                <h2>Experiences</h2>
                {
                    jsonData.Experiences.map(outerItem => {
                        return (
                            <div key={outerItem}>
                                <img src={outerItem.logo} alt="Logo" /><br/>
                                <a href={outerItem.url}>{outerItem.companyName}</a>
                                {
                                    outerItem.roles.map(innerItem => {
                                        return (
                                            <div key={innerItem}>
                                                <p>{innerItem.title}</p>
                                                <p>{innerItem.startDate} {innerItem.location}</p>
                                                <p>{innerItem.description}</p>
                                            </div> 
                                        )
                                    })}
                            </div>
                                
                            )
                        })
                    }
            </>
        )
    };
};
      
export default Example3;