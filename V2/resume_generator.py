import os
import re
from jinja2 import Environment, FileSystemLoader
import subprocess

def latex_escape(text):
    """
    Escapes special LaTeX characters in a given string.
    """
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

def generate_resume(data, template_file='template.tex', output_file='output_resume.tex'):
    """
    Renders the LaTeX resume template using the provided data and writes it to output_file.
    
    Parameters:
      data (dict): Resume data.
      template_file (str): Path to your LaTeX template.
      output_file (str): Name of the output .tex file.
      
    Returns:
      str: Path to the generated .tex file.
    """
    env = Environment(
        loader=FileSystemLoader('.'),
        variable_start_string='[[',   # custom start delimiter
        variable_end_string=']]',      # custom end delimiter
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

def compile_latex(tex_file):
    """
    Compiles a LaTeX file to PDF using pdflatex.
    
    Parameters:
      tex_file (str): Path to the .tex file.
      
    Returns:
      bytes or None: The compiled PDF as a byte string, or None if compilation fails.
    """
    # Command to compile using pdflatex
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
