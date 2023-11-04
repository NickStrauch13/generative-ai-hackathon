import React from 'react';

const StepBlock = ({ text, stepNumber }) => {
  return (
    <div className="step-block">
      <span className="step-number">{stepNumber}</span>
      <p className="step-text">{text}</p>
    </div>
  );
};

export default StepBlock;
