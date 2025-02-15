# ai_enhancer.py
import os
import requests
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("GOOGLE_AI_STUDIO_API_KEY")

def check_spelling_and_grammar(text):
    # Placeholder: Call your AI service for spelling/grammar correction here
    # For now, we return the text unmodified.
    return text

def enhance_ats(text):
    # Placeholder: Enhance the text for ATS compatibility via AI
    return text

def categorize_skills(skills_text):
    # Assume the input is a comma-separated string of skills.
    skills = [skill.strip() for skill in skills_text.split(',')]
    categories = {
        'Languages': [],
        'Frameworks': [],
        'Tools': [],
        'Platforms': [],
        'Soft Skills': []
    }
    # Basic categorization based on keywords; extend as needed.
    for skill in skills:
        lower_skill = skill.lower()
        if lower_skill in ['python', 'java', 'javascript']:
            categories['Languages'].append(skill)
        elif lower_skill in ['react', 'django', 'tensorflow']:
            categories['Frameworks'].append(skill)
        elif lower_skill in ['git', 'docker', 'vs code']:
            categories['Tools'].append(skill)
        elif lower_skill in ['linux', 'aws', 'windows']:
            categories['Platforms'].append(skill)
        else:
            categories['Soft Skills'].append(skill)
    
    # Remove any empty categories
    return {k: v for k, v in categories.items() if v}

def generate_descriptive_content(prompt):
    # Simulate a call to the Google AI Studio API to generate descriptive content.
    # Replace the URL and logic with your actual implementation.
    url = "https://google-ai-studio-endpoint.example.com/generate"
    headers = {"Authorization": f"Bearer {API_KEY}"}
    payload = {"prompt": prompt}
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        return response.json().get("content", "")
    else:
        return ""
