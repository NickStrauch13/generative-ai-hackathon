import React from 'react';
import StepBlock from "./StepBlock";

const InstructionSteps = ({ generatedSteps }) => {
  return (
    <div className="instruction-steps-container">
      {generatedSteps.length > 0 && (
        <ol>
          {generatedSteps.map((step, index) => (
            <li key={index}>
              <StepBlock text={step} />
            </li>
          ))}
        </ol>
      )}
    </div>
  );
};

export default InstructionSteps;