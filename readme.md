# LaTeX Resume Generator

A web application that generates professional PDF resumes from a clean dark UI. Fill in your details, use AI to polish descriptions, and download a LaTeX-compiled PDF in seconds.

## Features

- **Dark UI** — smooth dark theme with orange accents
- **AI-powered writing** — optimize experience, project, and publication descriptions with one click (powered by [Puter.js](https://puter.com), free, no API key needed)
- **AI skill categorization** — paste your skills and let AI sort them into Languages, Frameworks, Tools, Platforms, Soft Skills, and Others
- **LaTeX PDF generation** — compiles with `pdflatex` for a crisp, professional output
- **All resume sections** — Personal Info, Education, Skills, Experience, Projects, Publications, Honors, Volunteer, Certificates
- **Live PDF preview** — view the compiled PDF inline before downloading

## Prerequisites

- Python 3.8+
- A LaTeX distribution with `pdflatex`:
  - **Linux:** `sudo apt install texlive-full`
  - **Windows/macOS:** [MiKTeX](https://miktex.org) or [TeX Live](https://tug.org/texlive/)

## Installation

```bash
# Clone the repo
git clone https://github.com/your-username/latex-resume-generator.git
cd latex-resume-generator

# Install Python dependencies
pip install -r requirements.txt
```

## Usage

```bash
python app.py
```

Then open `http://localhost:5000` in your browser.

> The legacy Streamlit app is still available: `streamlit run main.py`

## File Structure

```
latex-resume-generator/
├── app.py                 # Flask web server
├── main.py                # Legacy Streamlit app
├── resume_generator.py    # LaTeX rendering + pdflatex compilation
├── ai_file.py             # AI prompt builders (used by Streamlit app)
├── template.tex           # Jinja2-powered LaTeX resume template
├── requirements.txt
├── templates/
│   └── index.html         # Main web UI
└── static/
    ├── css/style.css      # Dark orange theme
    └── js/main.js         # Form logic, AI integration, PDF preview
```

## How It Works

1. Fill in your resume sections in the browser form
2. Optionally click **AI Categorize** on skills or **Optimize with AI** on any description — Puter.js calls a free AI model directly from your browser
3. Click **Generate Resume** — the Flask backend renders the LaTeX template, runs `pdflatex`, and returns the PDF
4. Preview inline or click **Download PDF**
