import React, { useState } from "react";
import handleGenerateSteps from "../apis/generate_steps";

const MainContent = () => {

    const [textValue, setTextValue] = useState("");
    const [generatedSteps, setGeneratedSteps] = useState([]);

    const handleTextChange = (value) => {
        setTextValue(value);
    };

    const handleGenerateStepsClick = () => {
        handleGenerateSteps(textValue, setGeneratedSteps);
    };

    return (
        <div className="main-content">
            <div className="main-content-input-container">
                <input className="main-content-input-box" type="text" value={textValue} onChange={(e) => handleTextChange(e.target.value)} placeholder="Enter your text here..."/>
            </div>
            <button onClick={handleGenerateStepsClick}>Generate Steps</button>
            <div>
                {generatedSteps.length > 0 && (
                <ul>
                    {generatedSteps.map((step, index) => (
                    <li key={index}>{step}</li>
                    ))}
                </ul>
                )}
            </div>
        </div>
    )
}

export default MainContent;
