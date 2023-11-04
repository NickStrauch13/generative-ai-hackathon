import React, { useState } from "react";
import handleGenerateSteps from "../apis/generate_steps";
import InstructionSteps from "./InstructionSteps";
import Rating from "./Rating";

const MainContent = () => {

    const [textValue, setTextValue] = useState("");
    const [generatedSteps, setGeneratedSteps] = useState([]);
    const [youtubeLink, setYoutubeLink] = useState("");

    const handleTextChange = (value) => {
        setTextValue(value);
    };

    const handleGenerateStepsClick = () => {
        handleGenerateSteps(textValue, setGeneratedSteps, setYoutubeLink);
    };


    return (
        <div className="main-content">
            <div className="main-content-input-container">
                <input className="main-content-input-box" type="text" value={textValue} onChange={(e) => handleTextChange(e.target.value)} placeholder="Enter your text here..."/>
                <button className="main-content-submit-button" onClick={handleGenerateStepsClick}>Generate</button>
            </div>
            <Rating rating={3}/>
            <InstructionSteps generatedSteps={generatedSteps}/>
        </div>
    )
}

export default MainContent;
