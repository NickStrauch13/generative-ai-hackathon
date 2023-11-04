import React from 'react';

const EstimatedTime = ({ time }) => {
  return (
    <div className="estimated-time-text">
      <p>Estimated Time: {time} Minutes</p>
    </div>
  );
};

export default EstimatedTime;
