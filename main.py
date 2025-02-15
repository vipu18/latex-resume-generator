#libraries
import os
import re
import json
import streamlit as st
import subprocess
import tempfile
import base64

#functions
from resume_generator import generate_resume
from ai_file import (
    get_puter,
    removes,
    categorize,
    project_desc,
    publication_desc,
    experience_desc
)

#compile pdf
def compile_latex(latex_code):
    with tempfile.TemporaryDirectory() as tmpdir:
        tex_file = os.path.join(tmpdir, "document.tex")
        pdf_file = os.path.join(tmpdir, "document.pdf")
        
        with open(tex_file, "w", encoding="utf-8") as f:
            f.write(latex_code)
        
        cmd = ["pdflatex", "-interaction=nonstopmode", tex_file]
        process = subprocess.run(cmd, cwd=tmpdir, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        if process.returncode != 0:
            st.error("An error occurred during LaTeX compilation.")
            st.text("STDOUT:\n" + process.stdout.decode())
            st.text("STDERR:\n" + process.stderr.decode())
            return None
        
        with open(pdf_file, "rb") as f:
            pdf_bytes = f.read()
    return pdf_bytes

if "pdf_bytes" not in st.session_state:
    st.session_state.pdf_bytes = None

#skills cat
categories_list = ["Languages", "Frameworks", "Tools", "Platforms", "Soft Skills", "Others"]
for cat in categories_list:
    if cat not in st.session_state:
        st.session_state[cat] = ""

#main code
def main():
    st.title("LaTeX Resume Generator 📜")

#personal info
    st.header("Personal Information")
    name = st.text_input("Full Name", value="Jane Doe")
    email = st.text_input("Email", value="jane.doe@example.com")
    portfolio = st.text_input("Portfolio URL", value="janedoeportfolio.com")
    mobile = st.text_input("Mobile Number", value="+918765431210")
    github = st.text_input("Github URL", value="github.com/janedoe")
    linkedin = st.text_input("LinkedIn URL", value="linkedin.com/in/janedoe")

#education
    st.header("Education")
    edu_count = st.number_input("Number of Education Entries", min_value=0, value=1, step=1)
    education = []
    for i in range(int(edu_count)):
        st.subheader(f"Education Entry {i+1}")
        institution = st.text_input("Institution", value="Stanford University", key=f"edu_{i}_institution")
        edu_location = st.text_input("Location", value="Stanford, CA", key=f"edu_{i}_location")
        degree = st.text_input("Degree", value="Bachelor of Science in Computer Science", key=f"edu_{i}_degree")
        cgpa = st.text_input("cgpa", value="7.9", key=f"edu_{i}_cgpa")
        duration = st.text_input("Duration", value="September 2018 - June 2022", key=f"edu_{i}_duration")
        courses = st.text_input("Courses (comma separated)", 
                                value="Algorithms, Data Structures, Machine Learning, Web Development", 
                                key=f"edu_{i}_courses")
        if institution:
            education.append({
                "institution": institution,
                "location": edu_location,
                "degree": degree,
                "cgpa": cgpa,
                "duration": duration,
                "courses": [c.strip() for c in courses.split(",")] if courses else []
            })

#skills
    st.header("Skills")
    raw_skills = st.text_input("Enter your skills (comma separated)",
        "Python, Java, JavaScript, React, Django, TensorFlow, Git, Docker, VS Code, Linux, AWS, Windows, Leadership, Teamwork, Communication")
    
    if st.button("AI Categorize Skills"):
        prompt = categorize(raw_skills)
        st.markdown("**AI Output (JSON)**")
        get_puter(prompt, height=200)

    st.write("Paste AI JSON below and click 'Load JSON' to auto-fill categories")
    ai_json = st.text_area("AI JSON Output", "", height=100)

    if st.button("Load JSON"):
        try:
            data = removes(ai_json)
            for cat in categories_list:
                items = data.get(cat, [])
                st.session_state[cat] = ", ".join(items)
            st.success("Successfully loaded JSON into category fields below!")
        except:
            st.error("Invalid JSON. Please check formatting.")

    st.subheader("Categorized Skills (Auto-Filled)")
    col1, col2 = st.columns(2)
    with col1:
        st.session_state["Languages"] = st.text_area("Languages", st.session_state["Languages"], height=68)
        st.session_state["Frameworks"] = st.text_area("Frameworks", st.session_state["Frameworks"], height=68)
        st.session_state["Tools"] = st.text_area("Tools", st.session_state["Tools"], height=68)
    with col2:
        st.session_state["Platforms"] = st.text_area("Platforms", st.session_state["Platforms"], height=68)
        st.session_state["Soft Skills"] = st.text_area("Soft Skills", st.session_state["Soft Skills"], height=68)
        st.session_state["Others"] = st.text_area("Others", st.session_state["Others"], height=68)

    # Build a skills dict
    skills = {}
    for cat in categories_list:
        if st.session_state[cat]:
            arr = [x.strip() for x in st.session_state[cat].split(",") if x.strip()]
            if arr:
                skills[cat] = arr

#exp
    st.header("Experience")
    exp_count = st.number_input("Number of Experience Entries", min_value=0, value=1, step=1)
    experience = []
    for i in range(int(exp_count)):
        st.subheader(f"Experience Entry {i+1}")
        company = st.text_input("Company", value="Google", key=f"exp_{i}_company")
        exp_location = st.text_input("Location", value="Mountain View, CA", key=f"exp_{i}_location")
        role = st.text_input("Role", value="Software Engineer Intern", key=f"exp_{i}_role")
        duration = st.text_input("Duration", value="June 2021 - August 2021", key=f"exp_{i}_duration")
        detail_title = st.text_input("Experience Title", value="Search Algorithm Optimization", key=f"exp_{i}_detail_title")
        detail_description = st.text_area("Experience Description",
                                          value="Improved search ranking algorithms by 15% using machine learning.",
                                          key=f"exp_{i}_detail_description")

        # Single button for short experience desc with grammar+ATS
        if st.button(f"Generate Exp Desc {i+1}"):
            short_prompt = experience_desc(company, detail_description)
            st.markdown(f"** Experience Description {i+1}:**")
            get_puter(short_prompt, height=200)

        if company:
            experience.append({
                "company": company,
                "location": exp_location,
                "role": role,
                "duration": duration,
                "details": [{
                    "title": detail_title,
                    "description": detail_description
                }]
            })

#projects
    st.header("Projects")
    proj_count = st.number_input("Number of Project Entries", min_value=0, value=1, step=1)
    projects = []
    for i in range(int(proj_count)):
        st.subheader(f"Project Entry {i+1}")
        project_title = st.text_input("Project Title", value="Resume Generator", key=f"proj_{i}_title")
        project_description = st.text_area("Project Description",
                                           value="Built a web app to generate LaTeX resumes using AI for grammar and ATS optimization.",
                                           key=f"proj_{i}_description")
        tech_stack_str = st.text_input("Tech Stack (comma separated)",
                                       value="LaTeX, Python, AI",
                                       key=f"proj_{i}_tech_stack")
        tech_list = [t.strip() for t in tech_stack_str.split(",") if t.strip()]

        # project desc with grammar+ATS
        if st.button(f"Optimize Description {i+1}"):
            short_prompt = project_desc(project_title, "", project_description)
            st.markdown(f"**Project Description {i+1}:**")
            get_puter(short_prompt, height=300)

        projects.append({
            "title": project_title,
            "description": project_description,
            "tech_stack": tech_list
        })

#publication
    st.header("Publications")
    pub_count = st.number_input("Number of Publication Entries", min_value=0, value=1, step=1)
    publications = []
    for i in range(int(pub_count)):
        st.subheader(f"Publication Entry {i+1}")
        pub_title = st.text_input("Publication Title", value="AI in Resume Optimization", key=f"pub_{i}_title")
        pub_description = st.text_area("Publication Description",
                                       value="Research on using AI to improve resume quality and ATS compatibility.",
                                       key=f"pub_{i}_description")

        # Button for short publication description with grammar+ATS
        if st.button(f"Optimize Publication Description {i+1}"):
            short_pub = publication_desc(pub_title, pub_description)
            st.markdown(f"**Optimized Publication Description {i+1}:**")
            get_puter(short_pub, height=300)

        if pub_title:
            publications.append({
                "title": pub_title,
                "description": pub_description
            })

#honors
    st.header("Honors and Awards")
    honors_count = st.number_input("Number of Honors/Awards Entries", min_value=0, value=1, step=1)
    honors = []
    for i in range(int(honors_count)):
        st.subheader(f"Honor/Award Entry {i+1}")
        honor_title = st.text_input("Honor/Award Title", value="Student of the Year", key=f"honor_{i}_title")
        honor_year = st.text_input("Year", value="2025", key=f"honor_{i}_year")
        if honor_title:
            honors.append({
                "title": honor_title,
                "year": honor_year
            })

#volunteer
    st.header("Volunteer Experience")
    vol_count = st.number_input("Number of Volunteer Entries", min_value=0, value=1, step=1)
    volunteer = []
    for i in range(int(vol_count)):
        st.subheader(f"Volunteer Entry {i+1}")
        organization = st.text_input("Organization", value="Code for Good", key=f"vol_{i}_organization")
        vol_location = st.text_input("Location", value="San Francisco, CA", key=f"vol_{i}_location")
        vol_role = st.text_input("Role", value="Mentor", key=f"vol_{i}_role")
        vol_duration = st.text_input("Duration", value="January 2021 - December 2021", key=f"vol_{i}_duration")
        if organization:
            volunteer.append({
                "organization": organization,
                "location": vol_location,
                "role": vol_role,
                "duration": vol_duration
            })

#certificate
    st.header("Certificates")
    cert_count = st.number_input("Number of Certificate Entries", min_value=0, value=1, step=1)
    certificates = []
    for i in range(int(cert_count)):
        st.subheader(f"Certificate Entry {i+1}")
        cert_name = st.text_input("Certificate Name", value="AWS Certified Cloud Practitioner", key=f"cert_{i}_name")
        cert_issuer = st.text_input("Issuer", value="Amazon Web Services", key=f"cert_{i}_issuer")
        cert_link = st.text_input("Certificate Link", value="https://aws.amazon.com", key=f"cert_{i}_link")
        cert_start_end = st.text_input("Duration or Year", value="2023", key=f"cert_{i}_start_end")
        if cert_name:
            certificates.append({
                "name": cert_name,
                "issuer": cert_issuer,
                "link": cert_link,
                "start_end": cert_start_end
            })

#split skills in comma
    skills_dict = {}
    for cat, arr_str in st.session_state.items():
        if cat in categories_list and arr_str:
            splitted = [x.strip() for x in arr_str.split(",") if x.strip()]
            if splitted:
                skills_dict[cat] = splitted

#compile
    resume_data = {
        "name": name,
        "email": email,
        "portfolio": portfolio,
        "mobile": mobile,
        "github": github,
        "linkedin": linkedin,
        "education": education if education else None,
        "skills": skills_dict if skills_dict else None,
        "experience": experience if experience else None,
        "projects": projects if projects else None,
        "publications": publications if publications else None,
        "honors": honors if honors else None,
        "volunteer": volunteer if volunteer else None,
        "certificates": certificates if certificates else None
    }

#generate
    if st.button("Generate LaTeX Resume"):
        tex_file = generate_resume(resume_data)
        st.success(f"Resume generated: {tex_file}")
        
        with open(tex_file, "r", encoding="utf-8") as f:
            generated_tex = f.read()
        st.text_area("LaTeX Source", value=generated_tex, height=300)
        
        pdf_bytes = compile_latex(generated_tex)
        if pdf_bytes:
            st.success("PDF generated successfully!")
            b64_pdf = base64.b64encode(pdf_bytes).decode('utf-8')
            pdf_display = f'<iframe src="data:application/pdf;base64,{b64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'
            st.markdown(pdf_display, unsafe_allow_html=True)
            st.session_state.pdf_bytes = pdf_bytes
        else:
            st.error("Failed to compile PDF.")

#function call
if __name__ == "__main__":
    main()