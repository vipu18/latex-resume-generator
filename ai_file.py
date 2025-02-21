import json
import streamlit.components.v1 as components

def build_html(prompt: str) -> str:
    return f"""
    <html>
    <head>
      <style>
        html, body {{
          margin: 0; padding: 0;
          height: 100%;
        }}
        #result {{
          width: 100%;
          height: 100%;
          box-sizing: border-box;
          padding: 1rem;
        }}
        textarea {{
          width: 100%;
          height: 100%;
          background: #ffffff;
          color: #000000;
          border: 1px solid #ccc;
          font-family: sans-serif;
          white-space: pre-wrap;
          resize: none;
          outline: none;
          overflow-y: auto;
        }}
      </style>
    </head>
    <body>
      <div id="result">
        <textarea id="responseBox" readonly>Loading...</textarea>
      </div>
      <script src="https://js.puter.com/v2/"></script>
      <script>
        puter.ai.chat(`{prompt}`)
          .then(function(response){{
            document.getElementById("responseBox").value = response;
          }})
          .catch(function(error){{
            document.getElementById("responseBox").value = "Error: " + error;
          }});
      </script>
    </body>
    </html>
    """

def get_puter(prompt: str, height: int = 400):
    from streamlit.components.v1 import html
    final_html = build_html(prompt)
    return html(final_html, height=height)

def removes(ai_json: str):
    cleaned = ai_json.replace("```json", "").replace("```", "")
    return json.loads(cleaned)

def categorize(skills_input: str) -> str:
    return (
        "You are an AI assistant that categorizes a list of skills into these categories: "
        "Languages, Frameworks, Tools, Platforms, Soft Skills, or Others. "
        "Return the result in JSON format with keys 'Languages', 'Frameworks', 'Tools', 'Platforms', 'Soft Skills', and 'Others'. "
        "The skills are: '''" + skills_input + "'''"
    )

def project_desc(project_title: str, user_skills: str, project_desc: str) -> str:
    return (
        "You are an AI specialized in resume content. "
        "We have a project title, some additional skills, and a user-provided description. "
        "Fix grammar/spelling, optimize for ATS usage, and produce a final project description min 3 lines. "
        "Make it concise and engaging.\n\n"
        f"Project Title: {project_title}\n"
        f"User-Defined Skills: {user_skills}\n"
        f"User Project Description: {project_desc}"
    )

def publication_desc(pub_title: str, pub_desc: str) -> str:
    return (
        "You are specialized in resume content. "
        "We have a publication title and a user-provided description. "
        "Fix grammar/spelling, optimize for ATS usage, and produce a final publication description min 3 lines. "
        "Make it concise and engaging.\n\n"
        f"Publication Title: {pub_title}\n"
        f"User Publication Description: {pub_desc}"
    )

def experience_desc(company: str, detail_desc: str) -> str:
    return (
        "You are an AI specialized in resume content. "
        "We have a user-provided experience description for a company. "
        "Fix grammar/spelling, optimize for ATS usage, and produce a final experience description min 3 lines. "
        "Make it concise and engaging.\n\n"
        f"Company: {company}\n"
        f"Experience Description: {detail_desc}"
    )
