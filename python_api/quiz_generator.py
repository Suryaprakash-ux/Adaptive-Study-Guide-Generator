# ==============================================================================
# File: python_api/quiz_generator.py
# Description: A dedicated module for all quiz generation logic.
# ==============================================================================

import random
import re
from collections import Counter
import spacy
import nltk
from nltk.corpus import wordnet as wn

# --- Initialize NLP Models ---
# This will run once when the server starts.
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    print("Downloading spaCy model...")
    import spacy.cli
    spacy.cli.download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

# --- Helper Functions for Quiz Generation ---
def preprocess(text):
    doc = nlp(text)
    sentences = [sent.text.strip() for sent in doc.sents if len(sent.text.split()) > 4]
    noun_chunks = [chunk.text for chunk in doc.noun_chunks]
    tokens = [token.lemma_.lower() for token in doc if token.is_alpha and not token.is_stop and token.pos_ in ("NOUN", "PROPN")]
    keyword_counts = Counter(tokens)
    keywords = [k for k, _ in keyword_counts.most_common(50)]
    return {"doc": doc, "sentences": sentences, "noun_chunks": noun_chunks, "keywords": keywords}

def wordnet_distractors(word, pos_tag='n', max_distractors=3):
    distractors = set()
    for syn in wn.synsets(word, pos=pos_tag):
        for lemma in syn.lemmas():
            name = lemma.name().replace('_', ' ')
            if name.lower() != word.lower():
                distractors.add(name)
        for hyper in syn.hypernyms():
            for lemma in hyper.lemmas():
                name = lemma.name().replace('_', ' ')
                if name.lower() != word.lower():
                    distractors.add(name)
    return list(distractors)[:max_distractors]

def fallback_distractors(answer, keywords, noun_chunks, n=3):
    cand = [k for k in keywords if k.lower() not in answer.lower()]
    choices = set(cand[:n])
    for c in noun_chunks:
        if len(choices) >= n: break
        if c.lower() not in answer.lower():
            choices.add(c)
    return list(choices)[:n]

def make_distractors(answer, state, n=3):
    token = answer.strip().split()[0]
    wn_candidates = wordnet_distractors(token.lower(), pos_tag='n', max_distractors=n)
    if len(wn_candidates) >= n:
        return wn_candidates
    fb = fallback_distractors(answer, state['keywords'], state['noun_chunks'], n=n)
    combined = list(dict.fromkeys(wn_candidates + fb))
    return combined[:n]

def select_answer_candidate(sentence):
    s_doc = nlp(sentence)
    if s_doc.ents:
        return s_doc.ents[0].text.strip()
    chunks = sorted([c.text.strip() for c in s_doc.noun_chunks], key=len, reverse=True)
    if chunks:
        return chunks[0]
    nouns = [t.text for t in s_doc if t.pos_ in ("NOUN", "PROPN")]
    return nouns[0] if nouns else None

def make_mcq_from_sentence(sentence, state, n_distractors=3):
    ans = select_answer_candidate(sentence)
    if not ans or ans.lower() in sentence.lower().split()[:2]: return None
    q_text = sentence.replace(ans, "______")
    distractors = make_distractors(ans, state, n=n_distractors)
    options = [ans] + distractors
    options = list(dict.fromkeys([opt.strip() for opt in options]))
    if len(options) < 2: return None
    random.shuffle(options)
    return {"type": "mcq", "question": q_text, "options": options, "answer": ans}

def make_tf_from_sentence(sentence, state, false_prob=0.5):
    if random.random() > false_prob:
        return {"type": "tf", "question": sentence, "answer": "True"}
    s_doc = nlp(sentence)
    swap_target = None
    if s_doc.ents:
        swap_target = s_doc.ents[0].text
    else:
        chunks = [c.text for c in s_doc.noun_chunks]
        swap_target = chunks[0] if chunks else None
    if not swap_target:
        return {"type": "tf", "question": sentence, "answer": "True"}
    distractors = make_distractors(swap_target, state, n=5)
    if not distractors:
        return {"type": "tf", "question": sentence, "answer": "True"}
    replacement = random.choice(distractors)
    false_statement = sentence.replace(swap_target, replacement)
    return {"type": "tf", "question": false_statement, "answer": "False"}

# --- Main Function to be Called by the API ---
def create_quiz_from_text(text, num_questions=10):
    """
    Takes a block of text and generates a quiz with a specified number of questions.
    """
    state = preprocess(text)
    candidates = []
    for sent in state['sentences']:
        mcq = make_mcq_from_sentence(sent, state)
        if mcq: candidates.append(mcq)
        if random.random() < 0.5:
            tf = make_tf_from_sentence(sent, state)
            if tf: candidates.append(tf)
    
    random.shuffle(candidates)
    final_quiz = []
    seen_questions = set()
    for q in candidates:
        if len(final_quiz) >= num_questions: break
        q_text = q['question'].strip().lower()
        if q_text not in seen_questions:
            seen_questions.add(q_text)
            final_quiz.append(q)
            
    return final_quiz
