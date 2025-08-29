**                                                                                  **Adaptive Study Guide Generator**

AI-powered personalized learning platform that extracts educational content from YouTube videos, summarizes it intelligently, explains it in a simplified manner, and generates adaptive quizzes to enhance student learning.

**Project Overview**
The Adaptive Study Guide Generator is an AI-driven e-learning platform designed to help learners understand topics from YouTube videos more effectively.

Takes a YouTube video URL (supports multiple languages).

Extracts text using advanced speech-to-text techniques.

Summarizes content into concise, structured notes using NLP models.

Explains content in a learner-friendly way.

Generates quizzes with 5–10 MCQs and True/False questions.

If a learner scores below 50%, the system re-summarizes the topic in simpler terms and regenerates the quiz.

The process repeats until the learner achieves mastery.

This ensures a personalized, adaptive, and effective learning experience.

**Objectives**
1)Automate text extraction and summarization from video content.
2)Enable personalized learning by dynamically adjusting difficulty based on quiz performance.
3)Provide interactive quizzes for self-assessment.
4)Deliver hands-on experience in AI, NLP, frontend, backend, and API integrations.

**Features**

- **Video-to-Text Extraction** → Extracts text from YouTube videos.  
- **Automatic Summarization** → Uses NLP to produce concise, easy-to-read notes.  
- **Simplified Explanations** → Generates easier summaries for struggling learners.  
- **Quiz Generation** → Creates **5–10 adaptive questions** from summarized content.  
- **Performance Feedback** → Re-summarizes content if the score is **below 50%**.  
- **Adaptive Learning** → Ensures learners gain **mastery** before moving ahead.  
- **API-driven Integration** → Uses **Flask REST APIs** for smooth communication between **frontend & backend**.  
- **Multi-language Support** → Works seamlessly on videos in **different languages**.  
- **User-friendly UI** → Built using **React.js** for an engaging and seamless experience.  


**Project Workflow**
FlowChart TD
    A[User Inputs YouTube Video URL] --> B[Video-to-Text Extraction]
    B --> C[Text Summarization & Explanation]
    C --> D[Quiz Generation]
    D --> E[User Takes Quiz]
    E --> F{Score >= 50%?}
    F -->|Yes| G[Show Results & Finish]
    F -->|No| H[Re-summarize with Easier Notes]
    H --> I[Regenerate Quiz]
    I --> E

**This adaptive pipeline ensures continuous improvement in understanding.**

**Tech Stack**
## 🛠 Tech Stack  

| **Component**       | **Technology Used**                                       |
|---------------------|-----------------------------------------------------------|
| **Frontend**        | React.js, HTML5, CSS3, JavaScript                         |
| **Backend**         | Flask (Python)                                            |
| **AI / NLP**        | Hugging Face Transformers, SpaCy, NLTK, OpenAI/Google APIs|
| **Database**        | MongoDB / Firebase *(if used)*                            |
| **API Integration** | YouTube Transcript API, Custom Flask APIs                 |
| **Version Control** | Git, GitHub                                               |
| **Deployment**      | GitHub / Heroku / Render                                  |


**Installation & Setup**

1. Clone the Repository
git clone https://github.com/<your-username>/Adaptive-Study-Guide-Generator.git
cd Adaptive-Study-Guide-Generator

2. Set Up the Backend (Flask)
cd backend
pip install -r requirements.txt
python app.py

3. Set Up the Frontend (React)
cd frontend
npm install
npm start

4. Configure API Keys
Get a YouTube Transcript API key
Set up API keys in the .env file.

**API Integrations**

YouTube Transcript API → Extracts spoken content from video.

Flask REST APIs → Handles backend requests between frontend and AI modules.

NLP Libraries (Hugging Face, SpaCy, NLTK) → Summarization, explanation, and quiz generation.

**Modules & Responsibilities**
Module	Owner	Responsibility
Video-to-Text Extraction	Person 1	Extracts transcript from YouTube video URLs
Text Summarization & Explanation	Person 2	Summarizes content & prepares simplified explanations
Quiz Generation	You	Generates 5–10 adaptive quiz questions (MCQs & True/False)
Adaptive Learning & Feedback	Person 4	Re-summarizes text & regenerates quizzes based on user performance

**Adaptive Learning Logic**

If score ≥ 50% → Show results, mark topic as completed.

If score < 50% →

-> Simplify the summarized notes further.
-> Regenerate a new quiz with easier questions.
-> Allow the student to retry until mastery is achieved.
-> This ensures a personalized learning experience tailored to individual performance.

**Team Members**

| **Name**         | **Role**                   | **Contributions**                               |
|------------------|----------------------------|--------------------------------------------------|
| Bhavana Mahathi  | Video-to-Text Extraction   | Built module for transcript extraction           |
| Charan Teja      | Summarization              | Developed summarization and explanation module   |
| Surya Prakash    | Quiz Generation            | Created adaptive quiz generation module          |
| Pavan Ganesh     | Adaptive Feedback          | Implemented re-summarization and retry mechanism |


**Future Enhancements**

🔹 Add voice-based quizzes for interactive learning.
🔹 Use advanced LLMs for better question quality.
🔹 Support PDF/Document uploads in addition to YouTube links.
🔹 Implement user dashboards for tracking progress.
🔹 Multi-language text-to-speech for accessibility.

**License**
This project is licensed under the MIT License – feel free to use and modify with proper attribution.
