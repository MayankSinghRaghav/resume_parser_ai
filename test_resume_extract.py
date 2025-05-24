from resume_parser import extract_text_from_pdf
from skills_extractor import extract_skills
from info_extractor import extract_email, extract_phone, extract_name, extract_location
import json

text = extract_text_from_pdf(r"C:\Users\mayan\Desktop\resume_parser_ai\test_files\sample_resume.pdf")

resume_data = {
    "name": extract_name(text),
    "email": extract_email(text),
    "phone": extract_phone(text),
    "location": extract_location(text),
    "skills": extract_skills(text)
}

print(json.dumps(resume_data, indent=4))


