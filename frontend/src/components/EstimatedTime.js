import React from 'react';

const EstimatedTime = ({ time }) => {
  const titleStyle = {
    textDecoration: 'underline',
    textAlign: 'center',
    marginBottom: '0.5em', // This adds some space between the title and the cost
    alignItems: 'center',
    justifyContent: 'center',
    fontSize: '1.1em',
  };
  const timeStyle = {
    textAlign: 'center',
    marginBottom: '0.5em', // This adds some space between the title and the cost
    alignItems: 'center',
    justifyContent: 'center',
    fontSize: '1.1em',
  };
  return (
    <div className="estimated-time-text">
      <p style={titleStyle}>Estimated Time</p>
      <p style={timeStyle}> {time}</p>
    </div>
  );
};

export default EstimatedTime;
