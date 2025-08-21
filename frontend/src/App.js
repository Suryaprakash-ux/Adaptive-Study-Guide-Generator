import React, { useState } from 'react';
import Summarizer from './components/Summarizer';
import Quiz from './components/Quiz';
import Spinner from './components/Spinner';
import './App.css';

export default function App() {
    const [directText, setDirectText] = useState('');
    const [generatedNotes, setGeneratedNotes] = useState('');
    const [quiz, setQuiz] = useState(null);
    const [isLoadingNotes, setIsLoadingNotes] = useState(false);
    const [isLoadingQuiz, setIsLoadingQuiz] = useState(false);
    const [error, setError] = useState('');

    const handleGenerateNotes = async (e) => {
        e.preventDefault();
        setIsLoadingNotes(true);
        setError('');
        setGeneratedNotes('');
        setQuiz(null);

        try {
            if (!directText) throw new Error('Please paste some text to summarize.');

            const res = await fetch('http://localhost:5000/api/summarize', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ text: directText }),
            });
            if (!res.ok) {
                const errData = await res.json();
                throw new Error(errData.error || 'Failed to generate notes.');
            }
            const data = await res.json();
            setGeneratedNotes(data.notes);
        } catch (err) {
            setError(err.message);
        } finally {
            setIsLoadingNotes(false);
        }
    };

    const handleGenerateQuiz = async () => {
        setIsLoadingQuiz(true);
        setError('');
        setQuiz(null);
        try {
            // Use the original text for better quiz generation
            const textForQuiz = directText;
            const res = await fetch('http://localhost:5000/api/generate-quiz', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ text: textForQuiz }),
            });
            if (!res.ok) {
                const errData = await res.json();
                throw new Error(errData.error || 'Failed to generate quiz.');
            }
            const data = await res.json();
            if (data.quiz && data.quiz.length > 0) {
                setQuiz(data.quiz);
            } else {
                setError("Could not generate a quiz from the provided text.");
            }
        } catch (err) {
            setError(err.message);
        } finally {
            setIsLoadingQuiz(false);
        }
    };

    return (
        <div className="app-container">
            <div className="main-content">
                <div className="header">
                    <h1>AI Study Tools</h1>
                    <p>Generate structured notes and quizzes from any academic text.</p>
                </div>

                <Summarizer
                    directText={directText}
                    setDirectText={setDirectText}
                    handleGenerateNotes={handleGenerateNotes}
                    isLoadingNotes={isLoadingNotes}
                    generatedNotes={generatedNotes}
                    isLoadingQuiz={isLoadingQuiz}
                    handleGenerateQuiz={handleGenerateQuiz}
                />

                {error && (
                    <div className="error-message">
                        <p className="error-title">Error</p>
                        <p>{error}</p>
                    </div>
                )}
                
                {isLoadingQuiz && <Spinner text="Building your quiz..." />}
                
                {quiz && !isLoadingQuiz && (
                    <div className="quiz-section">
                        <Quiz quizData={quiz} />
                    </div>
                )}
            </div>
        </div>
    );
}