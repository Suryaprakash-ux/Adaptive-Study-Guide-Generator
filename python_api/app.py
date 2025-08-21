# ==============================================================================
# File: python_api/app.py
# Description: The main Flask server, now simplified.
# ==============================================================================

from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import traceback
# --- CHANGE: Import the new modules ---
from summarizer import generate_study_notes_with_api
from quiz_generator import create_quiz_from_text

# --- Load Environment Variables & Initialize ---
load_dotenv()
app = Flask(__name__)
CORS(app)

# --- API Endpoint for Summarization ---
@app.route('/api/summarize', methods=['POST'])
def summarize_text():
    data = request.get_json()
    text = data.get('text')
    if not text:
        return jsonify({'error': 'Text is required.'}), 400
    try:
        # --- CHANGE: Call the function from our new module ---
        notes = generate_study_notes_with_api(text)
        return jsonify({'notes': notes})
    except Exception as e:
        traceback.print_exc()
        return jsonify({'error': f'Failed to generate notes: {e}'}), 500

# --- API Endpoint for Quiz Generation ---
@app.route('/api/generate-quiz', methods=['POST'])
def generate_quiz():
    data = request.get_json()
    text = data.get('text')
    if not text:
        return jsonify({'error': 'Text is required to generate a quiz.'}), 400
    
    try:
        quiz = create_quiz_from_text(text)
        return jsonify({'quiz': quiz})
    except Exception as e:
        traceback.print_exc()
        return jsonify({'error': f'Failed to generate quiz: {e}'}), 500

# --- Main Flask App Runner ---
if __name__ == '__main__':
    app.run(debug=True, port=5000)
