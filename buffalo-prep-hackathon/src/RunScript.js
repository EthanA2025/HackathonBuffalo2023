import React, { useState, useEffect } from 'react'
import axios from 'axios'

const RunScript = () => {
    const [output, setOutput] = useState('');

    useEffect(() => {
        axios.get('http://localhost:5000/run_script')
            .then(res => {
                setOutput(res.data.output)
            })
            .catch(err => {
                console.error(err);
            });
    }, []);
    
    return (
        <div>
            <h1>output from regression model</h1>
            <pre>{output}</pre>
        </div>
    )
}


export default RunScript;