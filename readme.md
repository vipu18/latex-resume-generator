# LaTeX Resume Generator

## Overview
This project is a **LaTeX-based Resume Generator** that dynamically creates resumes using user-provided data. The system takes structured input and generates a well-formatted PDF resume using LaTeX templates.

## Features
- 📄 **Generate professional resumes** from structured data.
- 🏗 **Customizable LaTeX templates** to match different styles.
- ⚡ **Fast and automated** resume creation.
- 🖥 **Streamlit UI** for easy user interaction.

## Installation

### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- LaTeX distribution (TeX Live or MiKTeX)

### Install Dependencies
```bash
pip install -r requirements.txt
```

## Usage
### 1️⃣ Run the Streamlit App
```bash
streamlit run app.py
```

## File Structure
```
📂 LaTeX-Resume-Generator
│-- 📂 templates/       # LaTeX template files
│-- 📂 data/            # Sample resume data (YAML, JSON, CSV)
│-- 📂 output/          # Generated PDF resumes
│-- app.py             # Streamlit-based UI
│-- generate_resume.py # CLI script to generate resumes
│-- requirements.txt   # Python dependencies
│-- README.md          # Project documentation
```