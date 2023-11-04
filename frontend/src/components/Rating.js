import React from 'react';

const Rating = ({ rating }) => {
  const maxRating = 5;
  const filledCircles = Math.min(maxRating, parseInt(rating, 10));

  const getCircleColor = () => {
    if (rating <= 2) {
      return '#37b835'; // Green
    } else if (rating <= 4) {
      return '#ffc107'; // Yellow
    } else if (rating >= 5) {
      return '#dc3545'; // Red
    } else {
      return '#ccc'; // Default color for unknown ratings
    }
  };

  const getRatingDescription = () => {
    if (rating <= 2) {
      return 'Easy';
    } else if (rating <= 4) {
      return 'Medium';
    } else if (rating >= 5) {
      return 'Hard';
    } else {
      return ''; // Default description for unknown ratings
    }
  };

  const circles = [];
  for (let i = 1; i <= maxRating; i++) {
    const className = i <= filledCircles ? 'filled-circle' : 'empty-circle';
    const circleColor = i <= filledCircles ? getCircleColor() : '#ccc';
    circles.push(
      <div
        key={i}
        className={className}
        style={{ backgroundColor: circleColor }}
      ></div>
    );
  }

  const ratingTextColor = getCircleColor();
  const ratingDescription = getRatingDescription();
  const titleStyle = {
    textDecoration: 'underline',
    textAlign: 'center',
    marginBottom: '0.5em', // This adds some space between the title and the cost
    alignItems: 'center',
    justifyContent: 'center',
    fontSize: '1.5em',
    fontWeight: 'bold',
  };
  return (
    <div className="rating-container" style={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
        <p style={titleStyle}>Difficulty</p>
        <div className="rating-circles-container" style={{ display: 'flex', justifyContent: 'center' }}>
            {circles}
        </div>
        <p className="rating-text-description" style={{ color: ratingTextColor }}>({ratingDescription})</p>
    </div>
);

};

export default Rating;
