import React from 'react';

const Rating = ({ rating }) => {
  const maxRating = 5;
  const filledCircles = Math.min(maxRating, rating);

  const getCircleColor = () => {
    if (rating <= 3) {
      return '#37b835'; // Green
    } else if (rating === 4) {
      return '#ffc107'; // Yellow
    } else if (rating === 5) {
      return '#dc3545'; // Red
    } else {
      return '#ccc'; // Default color for unknown ratings
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

  return (
    <div className="rating-container">
        <div className="rating-circles-container">{circles}</div>
        <p className="rating-text" style={{ color: ratingTextColor }}>{rating}/5 Difficulty</p>
    </div>
  )
};

export default Rating;
