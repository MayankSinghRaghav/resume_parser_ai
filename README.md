# 🧠 Resume Parser AI

A powerful AI-based Resume Parser built using Python and NLP that extracts structured information such as name, email, phone, education, skills, and work experience from resumes in PDF format.

---

## 📌 Features

- ✅ Extracts key resume information automatically
- 🧾 Supports PDF format
- ⚙️ NLP-powered parsing (spaCy / NLTK / custom models)
- 📂 Batch processing of multiple resumes
- 🧠 Easily integratable with recruitment systems (ATS)
- 🔍 Clean, structured JSON/CSV output

---

## 🚀 Tech Stack

- Python 3.8+
- spaCy / NLTK
- PyMuPDF / pdfminer / pdfplumber
- Regex, Pandas
- Streamlit (optional for UI)
- FastAPI or Flask (optional API support)

---

## 📁 Folder Structure

```bash
resume_parser_ai/
├── data/                 # Sample resumes
├── outputs/              # Parsed results
├── parser/               # Core parsing logic
├── utils/                # Helper functions
├── app.py                # Entry-point script
├── requirements.txt
└── README.md
