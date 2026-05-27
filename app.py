from flask import Flask, render_template, request, jsonify
import tempfile, os, base64, shutil
from resume_generator import generate_resume, compile_latex

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/generate', methods=['POST'])
def generate():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided'}), 400

        tmpdir = tempfile.mkdtemp()
        try:
            shutil.copy(os.path.join(BASE_DIR, 'template.tex'), tmpdir)
            tex_path = os.path.join(tmpdir, 'output_resume.tex')
            generate_resume(data, template_file='template.tex', output_file=tex_path, base_dir=tmpdir)

            pdf_bytes = compile_latex(tex_path, output_dir=tmpdir)

            with open(tex_path, 'r', encoding='utf-8') as f:
                tex_source = f.read()

            if pdf_bytes:
                return jsonify({'success': True, 'pdf': base64.b64encode(pdf_bytes).decode(), 'tex': tex_source})
            else:
                return jsonify({'error': 'PDF compilation failed. Is pdflatex installed?', 'tex': tex_source}), 422
        finally:
            shutil.rmtree(tmpdir, ignore_errors=True)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
