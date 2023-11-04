import React, { useState } from "react";
import handleGenerateSteps from "../apis/generate_steps";
import InstructionSteps from "./InstructionSteps";
import Rating from "./Rating";
import EstimatedTime from "./EstimatedTime";
import EstimatedCost from "./EstimatedCost";

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
                <textarea className="main-content-input-box" rows="2" value={textValue} onChange={(e) => handleTextChange(e.target.value)} placeholder="What do you need to fix?"/>
                <button className="main-content-submit-button" onClick={handleGenerateStepsClick}>Generate</button>
            </div>
            <div className="main-content-info-container">
                <Rating rating={3}/>
                <EstimatedTime time={120}/>
                <EstimatedCost cost={80}/>
            </div>
            <InstructionSteps generatedSteps={generatedSteps}/>
        </div>
    )
}

export default MainContent;
