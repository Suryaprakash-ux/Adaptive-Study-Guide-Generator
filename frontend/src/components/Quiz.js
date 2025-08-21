import React, { useState } from 'react';
import styles from './Quiz.module.css'; // <-- Import CSS Module

const Quiz = ({ quizData }) => {
    const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
    const [userAnswers, setUserAnswers] = useState({});
    const [showResults, setShowResults] = useState(false);

    // ... (keep all the handler functions: handleAnswerSelect, handleNext, etc.)
    const handleAnswerSelect = (questionIndex, answer) => {
        setUserAnswers({ ...userAnswers, [questionIndex]: answer });
    };

    const handleNext = () => {
        if (currentQuestionIndex < quizData.length - 1) {
            setCurrentQuestionIndex(currentQuestionIndex + 1);
        }
    };

    const handleBack = () => {
        if (currentQuestionIndex > 0) {
            setCurrentQuestionIndex(currentQuestionIndex - 1);
        }
    };
    
    const handleSubmitQuiz = () => {
        setShowResults(true);
    };

    if (showResults) {
        let score = 0;
        quizData.forEach((q, index) => {
            if (userAnswers[index] === q.answer) {
                score++;
            }
        });

        return (
            <div className={styles.resultsContainer}>
                <h2>Quiz Results</h2>
                <p className={styles.score}>Your Score: {score} / {quizData.length}</p>
                <div className={styles.answersReview}>
                    {quizData.map((q, index) => (
                        <div key={index} className={styles.questionReview}>
                            <p><strong>Q{index + 1}:</strong> {q.question}</p>
                            <p className={userAnswers[index] === q.answer ? styles.correct : styles.incorrect}>
                                Your answer: {userAnswers[index] || "Not answered"}
                            </p>
                            {userAnswers[index] !== q.answer && <p className={styles.correct}>Correct answer: {q.answer}</p>}
                        </div>
                    ))}
                </div>
            </div>
        );
    }

    const currentQuestion = quizData[currentQuestionIndex];
    const options = currentQuestion.type === 'tf' ? ['True', 'False'] : currentQuestion.options;

    return (
        <div className={styles.quizContainer}>
            <h2>Test Your Knowledge</h2>
            <div className={styles.questionCard}>
                <p className={styles.questionText}><strong>Q{currentQuestionIndex + 1}:</strong> {currentQuestion.question}</p>
                <div className={styles.optionsContainer}>
                    {options.map((option, i) => (
                        <button
                            key={i}
                            className={`${styles.optionButton} ${userAnswers[currentQuestionIndex] === option ? styles.selected : ''}`}
                            onClick={() => handleAnswerSelect(currentQuestionIndex, option)}
                        >
                            {option}
                        </button>
                    ))}
                </div>
            </div>
            <div className={styles.quizNavigation}>
                <button onClick={handleBack} disabled={currentQuestionIndex === 0} className={styles.navButton}>Back</button>
                {currentQuestionIndex < quizData.length - 1 ? (
                    <button onClick={handleNext} className={styles.navButton}>Next</button>
                ) : (
                    <button onClick={handleSubmitQuiz} className={`${styles.navButton} ${styles.submitQuizBtn}`}>Submit Quiz</button>
                )}
            </div>
        </div>
    );
};

export default Quiz;