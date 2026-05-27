<p align="center"><h1 align="center">LATEX-RESUME-GENERATOR</h1></p>
<p align="center">
<em><code>❯ AI-Powered Professional Resume Generator with LaTeX Templates</code></em>
</p>
<p align="center">
<img src="https://img.shields.io/github/license/vipu18/latex-resume-generator?style=default&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
<img src="https://img.shields.io/github/last-commit/vipu18/latex-resume-generator?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
<img src="https://img.shields.io/github/languages/top/vipu18/latex-resume-generator?style=default&color=0080ff" alt="repo-top-language">
<img src="https://img.shields.io/github/languages/count/vipu18/latex-resume-generator?style=default&color=0080ff" alt="repo-language-count">
</p>
<p align="center"><!-- default option, no dependency badges. -->
</p>
<p align="center">
<!-- default option, no dependency badges. -->
</p>
<br>

##  Table of Contents

- [ Overview](#-overview)
- [ Features](#-features)
- [ Project Structure](#-project-structure)
  - [ Project Index](#-project-index)
- [ Getting Started](#-getting-started)
  - [ Prerequisites](#-prerequisites)
  - [ Installation](#-installation)
  - [ Usage](#-usage)
  - [ Testing](#-testing)
- [ Project Roadmap](#-project-roadmap)
- [ Contributing](#-contributing)
- [ License](#-license)
- [ Acknowledgments](#-acknowledgments)

---

##  Overview

The LaTeX Resume Generator is a sophisticated Streamlit-powered web application that transforms user input into professional PDF resumes using customizable LaTeX templates. This project combines the elegance of LaTeX typography with AI-powered content optimization to create ATS-compatible resumes with minimal effort.

The application features an intuitive web interface for collecting personal information, education history, work experience, projects, publications, and certifications. It leverages AI integration for automatic skill categorization and content enhancement, ensuring that resumes are both professionally formatted and optimized for Applicant Tracking Systems.

---

##  Features

<code>❯ **Core Functionality**</code>
- **Professional PDF Generation**: Creates polished resumes using LaTeX templates with proper typography
- **Streamlit Web Interface**: User-friendly interface for seamless data entry and resume customization
- **Real-time Compilation**: Automatic LaTeX-to-PDF conversion with error handling and preview
- **Comprehensive Sections**: Supports personal info, education, experience, projects, publications, honors, volunteer work, and certifications

<code>❯ **AI-Enhanced Features**</code>
- **Smart Skill Categorization**: AI-powered automatic organization of skills into Languages, Frameworks, Tools, Platforms, Soft Skills, and Others
- **Content Optimization**: Grammar correction, spelling fixes, and ATS optimization for descriptions
- **Dynamic Enhancement**: AI assistance for project descriptions, experience entries, and publication summaries

<code>❯ **Technical Features**</code>
- **Template Customization**: Flexible Jinja2-based LaTeX templates for easy modification
- **PDF Preview**: Built-in PDF viewer with download functionality
- **Session Management**: Persistent data storage during editing sessions
- **Error Handling**: Comprehensive LaTeX compilation error reporting and debugging

---

##  Project Structure

```sh
└── latex-resume-generator/
    ├── .gitignore
    ├── ai_file.py
    ├── main.py
    ├── output_resume.tex
    ├── readme.md
    ├── requirements.txt
    ├── resume_generator.py
    └── template.tex
```

###  Project Index
<details open>
<summary><b><code>LATEX-RESUME-GENERATOR/</code></b></summary>
<details> <!-- __root__ Submodule -->
<summary><b>__root__</b></summary>
<blockquote>
<table>
<tr>
<td><b><a href='https://github.com/vipu18/latex-resume-generator/blob/master/main.py'>main.py</a></b></td>
<td><code>❯ Streamlit application entry point with complete UI interface for resume data collection and PDF generation</code></td>
</tr>
<tr>
<td><b><a href='https://github.com/vipu18/latex-resume-generator/blob/master/resume_generator.py'>resume_generator.py</a></b></td>
<td><code>❯ Core resume generation engine handling LaTeX template processing, character escaping, and PDF compilation</code></td>
</tr>
<tr>
<td><b><a href='https://github.com/vipu18/latex-resume-generator/blob/master/ai_file.py'>ai_file.py</a></b></td>
<td><code>❯ AI integration module providing content optimization, skill categorization, and ATS enhancement features</code></td>
</tr>
<tr>
<td><b><a href='https://github.com/vipu18/latex-resume-generator/blob/master/template.tex'>template.tex</a></b></td>
<td><code>❯ Professional LaTeX resume template with Jinja2 syntax for dynamic content insertion and formatting</code></td>
</tr>
<tr>
<td><b><a href='https://github.com/vipu18/latex-resume-generator/blob/master/requirements.txt'>requirements.txt</a></b></td>
<td><code>❯ Python package dependencies including Streamlit, Jinja2, and document processing libraries</code></td>
</tr>
</table>
</blockquote>
</details>
</details>

---
##  Getting Started

###  Prerequisites

Before getting started with latex-resume-generator, ensure your runtime environment meets the following requirements:

- **Programming Language:** Python 3.8+
- **Package Manager:** Pip
- **LaTeX Distribution:** TeX Live, MiKTeX, or similar LaTeX compiler
- **System Requirements:** pdflatex command-line tool accessible in system PATH

###  Installation

Install latex-resume-generator using one of the following methods:

**Build from source:**

1. Clone the latex-resume-generator repository:
```sh
❯ git clone https://github.com/vipu18/latex-resume-generator
```

2. Navigate to the project directory:
```sh
❯ cd latex-resume-generator
```

3. Install the project dependencies:

**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style=default&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pip install -r requirements.txt
```

4. Verify LaTeX installation:
```sh
❯ pdflatex --version
```

###  Usage

Run latex-resume-generator using the following command:

**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style=default&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ streamlit run main.py
```

The application will launch in your default web browser at `http://localhost:8501`. Follow these steps:

1. **Personal Information**: Enter your name, contact details, and social profiles
2. **Education**: Add your educational background with institutions, degrees, and coursework
3. **Skills**: Input raw skills and use AI categorization for automatic organization
4. **Experience**: Document work experience with AI-powered description optimization
5. **Projects**: Showcase projects with technology stacks and enhanced descriptions
6. **Additional Sections**: Include publications, honors, volunteer work, and certifications
7. **Generate**: Click "Generate LaTeX Resume" to create and preview your PDF

###  Testing

Run the test suite using the following command:

**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style=default&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pytest
```

**Manual Testing:**
- Test LaTeX compilation: Verify pdflatex installation and template rendering
- UI Testing: Navigate through all form sections and validate input handling
- PDF Generation: Create sample resumes and verify PDF output quality

---
##  Project Roadmap

- [X] **`Core Resume Generation`**: <strike>Implement basic LaTeX template processing and PDF compilation</strike>
- [X] **`Streamlit Interface`**: <strike>Create user-friendly web interface for data collection</strike>
- [X] **`AI Integration`**: <strike>Add AI-powered content optimization and skill categorization</strike>
- [ ] **`Template Library`**: Expand template collection with multiple design options
- [ ] **`Export Formats`**: Add support for Word, HTML, and Markdown export formats
- [ ] **`Cloud Deployment`**: Deploy application to cloud platforms with file storage
- [ ] **`Resume Analytics`**: Implement ATS score analysis and improvement suggestions
- [ ] **`User Accounts`**: Add user registration and resume management system

---

##  Contributing

- **💬 [Join the Discussions](https://github.com/vipu18/latex-resume-generator/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/vipu18/latex-resume-generator/issues)**: Submit bugs found or log feature requests for the `latex-resume-generator` project.
- **💡 [Submit Pull Requests](https://github.com/vipu18/latex-resume-generator/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/vipu18/latex-resume-generator
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com/vipu18/latex-resume-generator/graphs/contributors">
      <img src="https://contrib.rocks/image?repo=vipu18/latex-resume-generator">
   </a>
</p>
</details>

---

##  License

This project is protected under the MIT License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

##  Acknowledgments

- **LaTeX Community**: For the robust typesetting system that powers professional document generation
- **Streamlit Team**: For providing an excellent framework for rapid web application development
- **Jinja2 Project**: For the flexible templating engine that enables dynamic content generation
- **AI Integration**: Leveraging modern AI capabilities for content optimization and enhancement
- **Open Source Contributors**: Thanks to all contributors who help improve this project
