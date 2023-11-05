import React from 'react';

const EstimatedCost = ({ cost }) => {
  const containerStyle = {
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    justifyContent: 'center'
  };

  const titleStyle = {
    textDecoration: 'underline',
    textAlign: 'center',
    marginBottom: '0.5em', // This adds some space between the title and the cost
    alignItems: 'center',
    justifyContent: 'center'
  };

  const costStyle = {
    fontSize: '1.5em',
    fontWeight: 'bold',
    alignItems: 'center',
    justifyContent: 'center',
    textAlign: 'center',

  };

  return (
    <div className="estimated-cost-container" style={containerStyle}>
      <p className="cost-title" style={titleStyle}>Estimated Cost</p>
      <p style={costStyle}>{cost}</p> 
    </div>
  );
};  

export default EstimatedCost;
