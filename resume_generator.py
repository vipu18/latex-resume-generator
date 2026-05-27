#libs
import os
import re
import shutil
from jinja2 import Environment, FileSystemLoader
import subprocess

def _find_pdflatex():
    found = shutil.which('pdflatex')
    if found:
        return found
    for candidate in [
        os.path.expanduser('~/bin/pdflatex'),
        '/usr/local/bin/pdflatex',
        '/usr/bin/pdflatex',
        '/opt/miktex/bin/pdflatex',
    ]:
        if os.path.isfile(candidate):
            return candidate
    raise FileNotFoundError("pdflatex not found. Install a LaTeX distribution (e.g. MiKTeX or TeX Live).")

#fucn to escape special LaTeX characters in a given string
def latex_escape(text):
    if not isinstance(text, str):
        return text
    # Paragraph breaks inside LaTeX macro arguments cause "Runaway argument" errors
    text = text.replace('\r\n', ' ').replace('\r', ' ').replace('\n', ' ')
    # Collapse multiple spaces
    import re as _re
    text = _re.sub(r'  +', ' ', text).strip()
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
def generate_resume(data, template_file='template.tex', output_file='output_resume.tex', base_dir='.'):
    env = Environment(
        loader=FileSystemLoader(base_dir),
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
def compile_latex(tex_file, output_dir=None):
    if output_dir is None:
        output_dir = os.path.dirname(os.path.abspath(tex_file))

    pdflatex = _find_pdflatex()
    cmd = [pdflatex, "-interaction=nonstopmode",
           f"-output-directory={output_dir}",
           os.path.abspath(tex_file)]
    process = subprocess.run(cmd, cwd=output_dir, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    stdout = process.stdout.decode()
    stderr = process.stderr.decode()
    print("pdflatex STDOUT:\n", stdout)
    print("pdflatex STDERR:\n", stderr)

    if process.returncode != 0:
        return None

    pdf_file = os.path.join(output_dir, os.path.splitext(os.path.basename(tex_file))[0] + ".pdf")
    with open(pdf_file, "rb") as f:
        return f.read()