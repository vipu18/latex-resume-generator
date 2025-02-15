# app.py
import streamlit as st
from resume_generator import generate_resume
from ai_enhancer import check_spelling_and_grammar, enhance_ats, categorize_skills, generate_descriptive_content

def main():
    st.title("LaTeX Resume Generator (Test Mode with Multiple Entries)")
    st.write("Fill in your information. You can add more than one entry in the optional sections.")

    # Personal Information
    st.header("Personal Information")
    name = st.text_input("Full Name", value="Jane Doe", key="name")
    email = st.text_input("Email", value="jane.doe@example.com", key="email")
    portfolio = st.text_input("Portfolio URL", value="janedoeportfolio.com", key="portfolio")
    mobile = st.text_input("Mobile Number", value="+1-987-654-3210", key="mobile")
    github = st.text_input("Github URL", value="github.com/janedoe", key="github")
    linkedin = st.text_input("LinkedIn URL", value="linkedin.com/in/janedoe", key="linkedin")

    # Education Section (Multiple Entries)
    st.header("Education")
    edu_count = st.number_input("Number of Education Entries", min_value=0, value=1, step=1, key="edu_count")
    education = []
    for i in range(int(edu_count)):
        st.subheader(f"Education Entry {i+1}")
        institution = st.text_input("Institution", value="Stanford University", key=f"edu_{i}_institution")
        edu_location = st.text_input("Location", value="Stanford, CA", key=f"edu_{i}_location")
        degree = st.text_input("Degree", value="Bachelor of Science in Computer Science", key=f"edu_{i}_degree")
        gpa = st.text_input("GPA", value="3.9", key=f"edu_{i}_gpa")
        duration = st.text_input("Duration (e.g., September 2018 - June 2022)", value="September 2018 - June 2022", key=f"edu_{i}_duration")
        courses = st.text_input("Courses (comma separated)", value="Algorithms, Data Structures, Machine Learning, Web Development", key=f"edu_{i}_courses")
        if institution:
            education.append({
                "institution": institution,
                "location": edu_location,
                "degree": degree,
                "gpa": gpa,
                "duration": duration,
                "courses": [course.strip() for course in courses.split(",")] if courses else []
            })

    # Skills Section (Single Input to be Categorized)
    st.header("Skills")
    skills_input = st.text_input(
        "Enter your skills (comma separated)",
        value="Python, Java, JavaScript, React, Django, TensorFlow, Git, Docker, VS Code, Linux, AWS, Windows, Leadership, Teamwork, Communication",
        key="skills_input"
    )
    skills = {}
    if skills_input:
        skills = categorize_skills(skills_input)

    # Experience Section (Multiple Entries)
    st.header("Experience")
    exp_count = st.number_input("Number of Experience Entries", min_value=0, value=1, step=1, key="exp_count")
    experience = []
    for i in range(int(exp_count)):
        st.subheader(f"Experience Entry {i+1}")
        company = st.text_input("Company", value="Google", key=f"exp_{i}_company")
        exp_location = st.text_input("Location", value="Mountain View, CA", key=f"exp_{i}_location")
        role = st.text_input("Role", value="Software Engineer Intern", key=f"exp_{i}_role")
        duration = st.text_input("Duration", value="June 2021 - August 2021", key=f"exp_{i}_duration")
        detail_title = st.text_input("Experience Title", value="Search Algorithm Optimization", key=f"exp_{i}_detail_title")
        detail_description = st.text_area(
            "Experience Description",
            value="Improved search ranking algorithms by 15% using machine learning.",
            key=f"exp_{i}_detail_description"
        )
        if company:
            # Apply AI enhancements to the experience description
            detail_description = check_spelling_and_grammar(detail_description)
            detail_description = enhance_ats(detail_description)
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

    # Projects Section (Multiple Entries)
    st.header("Projects")
    proj_count = st.number_input("Number of Project Entries", min_value=0, value=1, step=1, key="proj_count")
    projects = []
    for i in range(int(proj_count)):
        st.subheader(f"Project Entry {i+1}")
        project_title = st.text_input("Project Title", value="Resume Generator", key=f"proj_{i}_title")
        project_description = st.text_area(
            "Project Description",
            value="Built a web app to generate LaTeX resumes using AI for grammar and ATS optimization.",
            key=f"proj_{i}_description"
        )
        tech_stack = st.text_input(
            "Tech Stack (comma separated)",
            value="LaTeX, Python, AI",
            key=f"proj_{i}_tech_stack"
        )
        if project_title:
            # Optionally enhance the project description using AI
            if st.button(f"Enhance Project Description {i+1}", key=f"enhance_proj_{i}"):
                project_description = generate_descriptive_content(project_description)
            projects.append({
                "title": project_title,
                "description": project_description,
                "tech_stack": [tech.strip() for tech in tech_stack.split(",")] if tech_stack else []
            })

    # Publications Section (Multiple Entries)
    st.header("Publications")
    pub_count = st.number_input("Number of Publication Entries", min_value=0, value=1, step=1, key="pub_count")
    publications = []
    for i in range(int(pub_count)):
        st.subheader(f"Publication Entry {i+1}")
        pub_title = st.text_input("Publication Title", value="AI in Resume Optimization", key=f"pub_{i}_title")
        pub_description = st.text_area(
            "Publication Description",
            value="Research on using AI to improve resume quality and ATS compatibility.",
            key=f"pub_{i}_description"
        )
        if pub_title:
            publications.append({
                "title": pub_title,
                "description": pub_description
            })

    # Honors and Awards Section (Multiple Entries)
    st.header("Honors and Awards")
    honors_count = st.number_input("Number of Honors/Awards Entries", min_value=0, value=1, step=1, key="honors_count")
    honors = []
    for i in range(int(honors_count)):
        honor = st.text_input(f"Honor/Award {i+1}", value="Dean's List - 2022", key=f"honor_{i}")
        if honor:
            honors.append(honor)

    # Volunteer Experience Section (Multiple Entries)
    st.header("Volunteer Experience")
    vol_count = st.number_input("Number of Volunteer Entries", min_value=0, value=1, step=1, key="vol_count")
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

    # Compile the resume data dictionary; sections with no entries will be omitted.
    resume_data = {
        "name": name,
        "email": email,
        "portfolio": portfolio,
        "mobile": mobile,
        "github": github,
        "linkedin": linkedin,
        "education": education if education else None,
        "skills": skills if skills else None,
        "experience": experience if experience else None,
        "projects": projects if projects else None,
        "publications": publications if publications else None,
        "honors": honors if honors else None,
        "volunteer": volunteer if volunteer else None
    }

    if st.button("Generate LaTeX Resume", key="generate_resume"):
        output_file = generate_resume(resume_data)
        st.success(f"Resume generated: {output_file}")
        # Display the generated LaTeX code for review
        with open(output_file, "r", encoding="utf-8") as f:
            st.code(f.read(), language="latex")

if __name__ == '__main__':
    main()
