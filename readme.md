<p align="center">
  <h1 align="center">LaTeX Resume Generator</h1>
</p>
<p align="center">
  <em>AI-powered resume builder with a dark web UI and LaTeX PDF output</em>
</p>
<p align="center">
  <img src="https://img.shields.io/github/license/vipu18/latex-resume-generator?style=default&logo=opensourceinitiative&logoColor=white&color=f97316" alt="license">
  <img src="https://img.shields.io/github/last-commit/vipu18/latex-resume-generator?style=default&logo=git&logoColor=white&color=f97316" alt="last-commit">
  <img src="https://img.shields.io/github/languages/top/vipu18/latex-resume-generator?style=default&color=f97316" alt="top-language">
</p>

---

## Overview

A Flask web application that turns form input into a professionally typeset PDF resume. Fill in your details, use AI to polish descriptions, preview inline, and download — all from a smooth dark UI with orange accents.

---

## Features

**Resume builder**
- 9 sections: Personal Info, Education, Skills, Experience, Projects, Publications, Honors & Awards, Volunteer, Certificates
- Dynamic add / remove entries per section
- Live PDF preview after generation
- One-click PDF download

**AI writing tools** — powered by [Puter.js](https://puter.com), free with no API key
- Auto-categorize a raw skills list into Languages, Frameworks, Tools, Platforms, Soft Skills, and Others
- Optimize experience, project, and publication descriptions for ATS and grammar

**PDF engine**
- Jinja2-rendered LaTeX template compiled with `pdflatex`
- Special character escaping and newline sanitization to prevent compilation errors
- Full LaTeX source viewable in the UI

---

## Prerequisites

- Python 3.8+
- `pdflatex` on your PATH — install via:
  - **Linux:** `sudo apt install texlive-full`
  - **Windows / macOS:** [MiKTeX](https://miktex.org) or [TeX Live](https://tug.org/texlive/)

---

## Installation

```bash
git clone https://github.com/vipu18/latex-resume-generator
cd latex-resume-generator
pip install -r requirements.txt
```

---

## Usage

```bash
python app.py
```

Open `http://localhost:5000` in your browser.

> The original Streamlit app is still available: `streamlit run main.py`

---

## File Structure

```
latex-resume-generator/
├── app.py                  # Flask server — renders template, compiles PDF
├── resume_generator.py     # Jinja2 LaTeX rendering + pdflatex compilation
├── template.tex            # LaTeX resume template (Jinja2 syntax)
├── main.py                 # Legacy Streamlit app
├── ai_file.py              # AI prompt helpers (used by Streamlit app)
├── requirements.txt
├── templates/
│   └── index.html          # Web UI
└── static/
    ├── css/style.css       # Dark orange theme
    └── js/main.js          # Form logic, AI calls, PDF preview
```

---

## Tech Stack

| Layer     | Technology                        |
|-----------|-----------------------------------|
| Backend   | Python, Flask                     |
| Templating| Jinja2                            |
| PDF       | LaTeX / pdflatex (MiKTeX, TeX Live)|
| Frontend  | Vanilla HTML / CSS / JS           |
| AI        | Puter.js (free, in-browser)       |
