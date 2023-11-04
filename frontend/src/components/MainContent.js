import React, { useState } from "react";
import LoadingIcons from 'react-loading-icons'
import handleGenerateSteps from "../apis/generate_steps";
import InstructionSteps from "./InstructionSteps";
import Rating from "./Rating";
import EstimatedTime from "./EstimatedTime";
import EstimatedCost from "./EstimatedCost";

const MainContent = () => {

    const [textValue, setTextValue] = useState("");
    const [generatedSteps, setGeneratedSteps] = useState([]);
    const [youtubeLink, setYoutubeLink] = useState("");
    const [difficulty, setDifficulty] = useState("");
    const [time, setTime] = useState("");
    const [stepsAreLoading, setStepsAreLoading] = useState(false);
    const [infoIsLoading, setInfoIsLoading] = useState(false);
    const [hasGenerated, setHasGenerated] = useState(false);

    const handleTextChange = (value) => {
        setTextValue(value);
    };

    const handleGenerateStepsClick = () => {
        handleGenerateSteps(textValue, 
                            setGeneratedSteps, 
                            setYoutubeLink, 
                            setDifficulty, 
                            setTime,
                            setStepsAreLoading,
                            setInfoIsLoading,
                            setHasGenerated);
    };


    return (
        <div className="main-content">
            <div className="main-content-input-container">
                <textarea className="main-content-input-box" rows="2" value={textValue} onChange={(e) => handleTextChange(e.target.value)} placeholder="What do you need to fix?"/>
                <button className="main-content-submit-button" onClick={handleGenerateStepsClick}>Generate</button>
            </div>
            {!infoIsLoading && hasGenerated && (
              <div className="main-content-info-container">
                  <Rating rating={difficulty}/>
                  <EstimatedTime time={time}/>
                  <EstimatedCost cost={80}/>
                  {youtubeLink && (
                    <iframe
                        width="560"
                        height="315"
                        src={youtubeLink}
                        title="YouTube Tutorial"
                        allowFullScreen
                    ></iframe>
                    )}
              </div>
            )}
            {stepsAreLoading && <LoadingIcons.ThreeDots className="loading-icon" fill="#007bff" stroke="#704214"/>}
            {!stepsAreLoading && <InstructionSteps generatedSteps={generatedSteps}/>}
        </div>
    )
}

export default MainContent;
