# ==============================================================================
# File: python_api/summarizer.py
# Description: A dedicated module for all summarization logic.
# ==============================================================================

import google.generativeai as genai
from markdown_it import MarkdownIt
import os
import traceback

# --- Initialize API and Markdown Renderer ---
# This will run once when the server starts.
api_key = os.getenv("GEMINI_API_KEY")
md = MarkdownIt()
try:
    if api_key:
        genai.configure(api_key=api_key)
    else:
        print("WARNING: GEMINI_API_KEY not found in .env file. Summarizer will not work.")
except Exception as e:
    print(f"Error configuring API in summarizer.py: {e}")

def generate_study_notes_with_api(text):
    """
    Generates structured, formatted study notes from a given text
    by calling the Google Gemini API.
    """
    if not api_key:
        raise ValueError("API key is not configured.")
        
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    prompt = f"""
        As an expert academic tutor, create a set of structured exam notes in Markdown format from the provided text.
        The notes must contain different sections with bullet pointed matter in them and also important extra points which are not in the provided text.
        [Text to Process]
        {text}
        [Generated Notes]
    """
    
    response = model.generate_content(prompt)
    return response.text