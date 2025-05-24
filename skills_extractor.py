import spacy

# Load English NLP model
nlp = spacy.load("en_core_web_sm")

# Sample skill keywords (you can expand this list)
SKILL_KEYWORDS = {
    "python", "java", "c++", "machine learning", "deep learning", "django",
    "flask", "sql", "html", "css", "javascript", "react", "pandas", "numpy",
    "tensorflow", "pytorch", "nlp", "opencv", "git", "docker"
}

def extract_skills(resume_text):
    doc = nlp(resume_text.lower())
    extracted_skills = set()

    for token in doc:
        if token.text in SKILL_KEYWORDS:
            extracted_skills.add(token.text)

    return list(extracted_skills)
