import React from 'react';

const Spinner = ({ text }) => (
    <div className="spinner-container">
        <div className="spinner"></div>
        <p className="spinner-text">{text}</p>
    </div>
);

export default Spinner;