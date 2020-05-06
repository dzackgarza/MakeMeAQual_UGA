from flask import Flask, make_response
from flask_cors import CORS
from flask import request, Response, send_file
import subprocess
import io

app = Flask(__name__, static_folder="Frontend")
CORS(app)

pandoc_cmd_html = """
pandoc -f markdown --filter pandoc-include --filter pandoc-theorem-exe -r markdown+tex_math_dollars+simple_tables+table_captions+yaml_metadata_block+smart+blank_before_blockquote+backtick_code_blocks+link_attributes --lua-filter=/home/zack/Notes/Latex/dollar_math.lua -s --mathjax
"""

pandoc_cmd_pdf = """
pandoc -f markdown --filter pandoc-include --filter pandoc-theorem-exe -r markdown+tex_math_dollars+simple_tables+table_captions+yaml_metadata_block+smart+blank_before_blockquote+backtick_code_blocks+link_attributes --template=/home/zack/Notes/Latex/pandoc_template.tex  --resource-path="$directory" --pdf-engine=pdflatex --lua-filter=/home/zack/Notes/Latex/dollar_math.lua -t pdf
"""

@app.route('/createqual', methods=['POST'])
def example():
    content = request.get_json()
    questions = content['questions']
    to_pdf = True #content['pdf'] == 1
    print(to_pdf)
    total_string = ""
    print(to_pdf == 1)
    pandoc_cmd = pandoc_cmd_pdf if to_pdf else pandoc_cmd_pdf 
    for i, x in enumerate(questions):
        out_str = '# Question {q_number}\n\n{content}\n\n'.format(q_number = i+1, content = x)
        total_string += out_str
    final_cmd = "echo \'{total_string}\' | {pandoc_cmd}".format(total_string=total_string, pandoc_cmd=pandoc_cmd)
    p = subprocess.Popen(final_cmd, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    p.wait()
    print(output)
    if (to_pdf):
        f = open('mf.pdf', 'w+b')
        binary_format = bytearray(output)
        f.write(binary_format)
        f.close()
        # response = make_response(image_binary)
        # response.headers.set('Content-Type', 'application/pdf')
        # response.headers.set('Content-Disposition', 'attachment', filename='Qual.pdf')
        mem = io.BytesIO(binary_format) 
        # response = send_file(
        # mem,
        # as_attachment=True,
        # attachment_filename='out.pdf',
        # mimetype='application/pdf'
        # )
        response = make_response(bytearray(output.encode))
        response.headers.set('Content-Disposition', 'attachment', filename='qualout.pdf')
        response.headers.set('Content-Type', 'application/pdf')
        return response
        # return send_file(, attachment_filename="qual.pdf", mimetype="application/pdf")
        # resp= Response(io.BytesIO(output)) 
        # resp.headers['Content-Disposition'] = "inline; filename=%s" % "Qual.pdf" 
        # resp.mimetype = 'application/pdf'
        # return(resp)
    else:
        return(output)

if __name__ == '__main__':
    app.run(port = 5000, debug=True)

















