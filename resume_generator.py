#libs
import os
import re
from jinja2 import Environment, FileSystemLoader
import subprocess

#fucn to escape special LaTeX characters in a given string
def latex_escape(text):
    if not isinstance(text, str):
        return text
    conv = {
        '&': r'\&',
        '%': r'\%',
        '$': r'\$',
        '#': r'\#',
        '_': r'\_',
        '{': r'\{',
        '}': r'\}',
        '~': r'\textasciitilde{}',
        '^': r'\textasciicircum{}',
        '\\': r'\textbackslash{}',
    }
    pattern = re.compile('|'.join(re.escape(k) for k in conv.keys()))
    return pattern.sub(lambda m: conv[m.group()], text)

#render the file
def generate_resume(data, template_file='template.tex', output_file='output_resume.tex'):
    env = Environment(
        loader=FileSystemLoader('.'),
        variable_start_string='[[',   
        variable_end_string=']]',     
        block_start_string='[%',
        block_end_string='%]',
        comment_start_string='<#',
        comment_end_string='#>'
    )
    env.filters['latex_escape'] = latex_escape

    template = env.get_template(template_file)
    rendered_tex = template.render(**data)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(rendered_tex)

    return output_file

#compile the file to pdf using pdflatex
def compile_latex(tex_file):
    cmd = ["pdflatex", "-interaction=nonstopmode", tex_file]
    process = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    stdout = process.stdout.decode()
    stderr = process.stderr.decode()
    print("pdflatex STDOUT:\n", stdout)
    print("pdflatex STDERR:\n", stderr)
    
    if process.returncode != 0:
        return None

    pdf_file = os.path.splitext(tex_file)[0] + ".pdf"
    with open(pdf_file, "rb") as f:
        pdf_bytes = f.read()
    return pdf_bytes