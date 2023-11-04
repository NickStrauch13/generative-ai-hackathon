import React, { useState } from "react";


const MainContent = () => {

    const [textValue, setTextValue] = useState("");

    const handleTextChange = (value) => {
        setTextValue(value);
    };

    return (
        <div className="main-content">
            <div className="main-content-input-container">
                <input className="main-content-input-box" type="text" value={textValue} onChange={(e) => handleTextChange(e.target.value)} placeholder="Enter your text here..."/>
                <p>{textValue}</p>
            </div>
        </div>
    )
}

export default MainContent