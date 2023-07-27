import React from 'react';
import jsonData from '../data-ex1.json'

class Example1 extends React.Component {

    render() {
        return(
            <>
                <h2>Skills</h2>
                    {
                        jsonData.Skills.map(outerItem => {
                            return (
                                <>
                                    <h4 key={outerItem}>{outerItem.Area}</h4>
                                    <ul>
                                        {outerItem.SkillSet.map(innerItem => {
                                            return innerItem.Hot ? <li key={outerItem}>{innerItem.Name}</li> : null;
                                        })}
                                    </ul>
                                </>
                            )
                        })
                    }
            </>
        )
    };
};
      
export default Example1;