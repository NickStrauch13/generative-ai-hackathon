import React, {useState} from 'react';
import handleElaborate from '../apis/elaborate';
import LoadingIcons from 'react-loading-icons'

const StepBlock = ({ text, stepNumber }) => {

  const [elaboration, setElaboration] = useState("");
  const [hasElaborated, setHasElaborated] = useState(false);
  const [isElaborating, setIsElaborating] = useState(false);

  const handleStepClick = () => {
    handleElaborate(text, setElaboration, setHasElaborated, setIsElaborating);
  }

  return (
    <div className="step-block-outer">
      <div className="step-block" onClick={handleStepClick}>
        <span className="step-number">{stepNumber}</span>
        <p className="step-text">{text}</p>
      </div>
      {!isElaborating && hasElaborated && <p className="step-elaboration">{elaboration}</p>}
      {isElaborating && <LoadingIcons.ThreeDots className="loading-icon-elaborate" fill="#007bff"/>}
    </div>
  );
};

export default StepBlock;
