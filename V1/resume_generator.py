# resume_generator.py
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
    env = Environment(
        loader=FileSystemLoader('.'),
        variable_start_string='[[',
        variable_end_string=']]',
        block_start_string='[%',
        block_end_string='%]',
        comment_start_string='<#',
        comment_end_string='#>'
    )
    # Register the LaTeX escape filter
    env.filters['latex_escape'] = latex_escape

    template = env.get_template(template_file)
    rendered_tex = template.render(**data)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(rendered_tex)

    # Optionally compile to PDF if pdflatex is available
    # subprocess.run(["pdflatex", output_file])

    return output_file
