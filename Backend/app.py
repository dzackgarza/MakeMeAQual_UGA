from flask import Flask, make_response
from flask_cors import CORS
from flask import request, Response, send_file
import subprocess
import io

app = Flask(__name__, static_folder="Frontend")
CORS(app)

pandoc_cmd_html = """
pandoc -f markdown --filter pandoc-include --filter pandoc-theorem-exe -r markdown+tex_math_dollars+simple_tables+table_captions+yaml_metadata_block+smart+blank_before_blockquote+backtick_code_blocks+link_attributes --lua-filter=/home/zack/Notes/Latex/dollar_math.lua --template=./webpage_template.html -s --mathjax
"""

pandoc_cmd_pdf = """
pandoc -f markdown --filter pandoc-include --filter pandoc-theorem-exe -r markdown+tex_math_dollars+simple_tables+table_captions+yaml_metadata_block+smart+blank_before_blockquote+backtick_code_blocks+link_attributes --template=/home/zack/Notes/Latex/pandoc_template.tex  --resource-path="$directory" --pdf-engine=pdflatex --lua-filter=/home/zack/Notes/Latex/dollar_math.lua -t pdf
"""

@app.route('/createqual', methods=['POST'])
def example():
    content = request.get_json()
    questions = content['questions']
    to_pdf = content['do_pdf'] == 1
    print("To PDF? ", to_pdf)
    total_string =  open('./latexmacs.tex', 'r').read() + "\n"
    # total_string = "\\newcommand{\ZZ}[0]{{\mathbb{Z}}}\n\n" 
    pandoc_cmd = pandoc_cmd_pdf if to_pdf else pandoc_cmd_html
    for i, x in enumerate(questions):
        out_str = '# Question {q_number}\n\n{content}\n\n'.format(
                q_number = i+1, 
                content = x
            )
        total_string += out_str
    final_cmd = "echo \'{total_string}\' | {pandoc_cmd}".format(
            total_string = total_string, 
            pandoc_cmd = pandoc_cmd
        )
    p = subprocess.Popen(final_cmd, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    p.wait()
    if (to_pdf):
        response = make_response(bytearray(output))
        response.headers.set('Content-Disposition', 'attachment', filename='qualout.pdf')
        response.headers.set('Content-Type', 'application/pdf')
        return response
    else:
        print(output)
        return(output)

if __name__ == '__main__':
    app.run(port = 5000, debug=True)

















