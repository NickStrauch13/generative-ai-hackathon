import React, {useState} from 'react';
import handleElaborate from '../apis/elaborate';


const StepBlock = ({ text, stepNumber }) => {

  const [elaboration, setElaboration] = useState("");
  const [hasElaborated, setHasElaborated] = useState(false);

  const handleStepClick = () => {
    handleElaborate(text, setElaboration, setHasElaborated);
  }

  return (
    <div className="step-block" onClick={handleStepClick}>
      <span className="step-number">{stepNumber}</span>
      <p className="step-text">{text}</p>
      {hasElaborated && <p className="step-elaboration">{elaboration}</p>}
    </div>
  );
};

export default StepBlock;
