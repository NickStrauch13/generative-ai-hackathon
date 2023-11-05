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
    const [cost, setCost] = useState("");
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
                            setCost,
                            setStepsAreLoading,
                            setInfoIsLoading,
                            setHasGenerated);
    };


    return (
        <div className="main-content">
            <div className="main-content-input-container">
                <textarea className="main-content-input-box" rows="2" value={textValue} onChange={(e) => handleTextChange(e.target.value)} placeholder="I need to fix..."/>
                <button className="main-content-submit-button" onClick={handleGenerateStepsClick}>Generate</button>
            </div>
            {!infoIsLoading && hasGenerated && (
              <div className="main-content-info-container">
                  <Rating rating={difficulty}/>
                  <EstimatedTime time={time}/>
                  <EstimatedCost cost={cost}/>
                  {youtubeLink && (
                        <div className="main-content-youtube-frame">
                            <iframe 
                                title="YouTube Video"
                                width="410" 
                                height="231" 
                                src={youtubeLink}
                                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
                                allowFullScreen>
                            </iframe>
                        </div>
                    )}

              </div>
            )}
            {(stepsAreLoading || infoIsLoading) && <LoadingIcons.ThreeDots className="loading-icon" fill="#007bff"/>}
            {!stepsAreLoading && <InstructionSteps generatedSteps={generatedSteps}/>}
        </div>
    )
}

export default MainContent;
