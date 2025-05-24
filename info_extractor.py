import spacy
import re

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

def extract_email(text):
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    matches = re.findall(email_pattern, text)
    return matches[0] if matches else None

def extract_phone(text):
    phone_pattern = r'(\+?\d{1,3}[\s-]?)?\(?\d{2,5}\)?[\s-]?\d{6,10}'
    matches = re.findall(phone_pattern, text)
    return matches[0] if matches else None

def extract_name(text):
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text
    return None

def extract_location(text):
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "GPE":
            return ent.text
    return None
