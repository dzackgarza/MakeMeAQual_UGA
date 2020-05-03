from flask import Flask
from flask_cors import CORS
from flask import request
import subprocess

app = Flask(__name__, static_folder="Frontend")
CORS(app)


@app.route('/createqual', methods=['POST'])
def example():
    print (request)
    content = request.get_json()
    total_string = ""
    for i, x in enumerate(content):
        out_str = '# Question {q_number}\n\n{content}\n\n'.format(q_number = i+1, content = x)
        print("----------------")
        total_string += out_str
    print(total_string)
    return 'JSON posted'
    # language = request.args.get('language') #if key doesn't exist, returns None
    # framework = request.args['framework'] #if key doesn't exist, returns a 400, bad request error
    # website = request.args.get('website')

    # return '''<h1>The language value is: {}</h1>
              # <h1>The framework value is: {}</h1>
              # <h1>The website value is: {}'''.format(language, framework, website)

if __name__ == '__main__':
    app.run(port = 5000, debug=True)

















