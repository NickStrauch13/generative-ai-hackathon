import React from 'react';
import StepBlock from "./StepBlock";

const InstructionSteps = ({ generatedSteps }) => {
  return (
    <div className="instruction-steps-container">
      {generatedSteps.length > 0 && (
        <ul style={{ listStyleType: 'none' }}>
          {generatedSteps.map((step, index) => (
            <li key={index}>
              <StepBlock text={step} stepNumber={index + 1} />
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default InstructionSteps;