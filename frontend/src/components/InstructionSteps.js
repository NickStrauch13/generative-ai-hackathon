import React from 'react';

const InstructionSteps = ({ generatedSteps }) => {
  return (
    <div className="instruction-steps-container">
      {generatedSteps.length > 0 && (
        <ol>
          {generatedSteps.map((step, index) => (
            <li key={index}>{step}</li>
          ))}
        </ol>
      )}
    </div>
  );
};

export default InstructionSteps;