import React, { useState, useEffect } from 'react';
import data from '../postData.json'

const PostList = () => {
    const[postData, setPostData] = useState([]);

    useEffect(() => {
        setPostData(data)
    }, []);

    return (
        <>
            {
                postData.map(item => {
                    return (
                        <div key={item.id}>
                            <h2>{item.title}</h2>
                            <h3>{item.content}</h3>
                        </div>
                    )
                })
            }
        </>
        
    );
};

export default PostList;