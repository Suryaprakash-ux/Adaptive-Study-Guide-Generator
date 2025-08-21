import React from 'react';
import ReactMarkdown from 'react-markdown';
import Spinner from './Spinner';
import styles from './Summarizer.module.css'; // <-- Import CSS Module

const Summarizer = ({
    directText,
    setDirectText,
    handleGenerateNotes,
    isLoadingNotes,
    generatedNotes,
    isLoadingQuiz,
    handleGenerateQuiz
}) => {
    return (
        <>
            <form onSubmit={handleGenerateNotes} className={styles.formContainer}>
                <div className={styles.textareaGroup}>
                    <label htmlFor="direct_text">Text to Process</label>
                    <textarea
                        id="direct_text"
                        className={styles.textarea}
                        rows="10"
                        value={directText}
                        onChange={(e) => setDirectText(e.target.value)}
                        placeholder="Paste your text here..."
                    ></textarea>
                </div>
                <button type="submit" disabled={isLoadingNotes} className={styles.generateButton}>
                    {isLoadingNotes ? 'Generating Notes...' : 'Generate Notes'}
                </button>
            </form>

            {isLoadingNotes && <Spinner text="Generating notes, please wait..." />}

            {generatedNotes && !isLoadingNotes && (
                <div className={styles.notesSection}>
                    <h2>Generated Notes</h2>
                    <div className={styles.prose}>
                        <ReactMarkdown>{generatedNotes}</ReactMarkdown>
                    </div>
                    <div className={styles.quizButtonContainer}>
                        <button onClick={handleGenerateQuiz} disabled={isLoadingQuiz} className={styles.quizButton}>
                            {isLoadingQuiz ? 'Generating Quiz...' : 'Generate Quiz'}
                        </button>
                    </div>
                </div>
            )}
        </>
    );
};

export default Summarizer;