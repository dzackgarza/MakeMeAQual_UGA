from flask import Flask, make_response
from flask_cors import CORS
from flask import request, Response, send_file
import subprocess
import io
import random


app = Flask(__name__, static_folder="Frontend")
CORS(app)

pandoc_cmd_html = """
pandoc -f markdown -r markdown+tex_math_dollars+simple_tables+table_captions+yaml_metadata_block+smart+blank_before_blockquote+backtick_code_blocks+link_attributes --lua-filter=/home/zack/Notes/Latex/dollar_math.lua -s --mathjax=https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-MML-AM_CHTML
"""

pandoc_cmd_pdf = """
pandoc -f markdown -r markdown+tex_math_dollars+simple_tables+table_captions+yaml_metadata_block+smart+blank_before_blockquote+backtick_code_blocks+link_attributes --template=/home/zack/Notes/Latex/pandoc_template.tex  --resource-path="$directory" --pdf-engine=pdflatex --lua-filter=/home/zack/Notes/Latex/dollar_math.lua -t latex -o out.pdf && cat out.pdf
"""
@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"

@app.route('/createqual', methods=['POST'])
def example():
    # Extract JSON data
    content = request.get_json()
    to_pdf = content['do_pdf'] == 1
    num_questions = content['num_questions']
    questions = random.sample(content['questions'], num_questions)
        
    # Start building markdown document
    total_string = "" if to_pdf else open('latexmacs.tex', 'r').read() + "\n\n"
    pandoc_cmd = pandoc_cmd_pdf if to_pdf else pandoc_cmd_html
    total_string += "---\ntitle: Qualifying Exam\n---\n\n"

    # Add all questions to doc
    for i, x in enumerate(questions):
        out_str = '# Question {q_number} (? {q_year}, {orig_number})\n\n{content}\n\n'.format(
                q_number = i+1,
                q_year = x['year'],
                orig_number = x['number'],
                content = x['question']
            ).replace("'", r"\textsc{\char13}")
        print(out_str)
        total_string += out_str
    #print(total_string)
    final_cmd = "printf \'\\n%s\' \'{total_string}\' | {pandoc_cmd}".format(
            total_string = total_string,
            pandoc_cmd = pandoc_cmd
        )
    print(final_cmd)
    p = subprocess.Popen(final_cmd, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    p.wait()
    print(output)
    if (to_pdf):
        response = make_response(bytearray(output))
        response.headers.set('Content-Disposition', 'attachment', filename='qualout.pdf')
        response.headers.set('Content-Type', 'application/pdf')
        return response
    else:
        return(output)

if __name__ == '__main__':
    app.run(host = '0.0.0.0')
    # app.run(host = '0.0.0.0', ssl_context=('/home/zack/cert.pem', '/home/zack/key.pem'))

















