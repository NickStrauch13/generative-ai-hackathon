import React from 'react';

const EstimatedCost = ({ cost }) => {
  return (
    <div className="estimated-cost-text">
      <p>Estimated Cost: ${cost}</p>
    </div>
  );
};

export default EstimatedCost;
