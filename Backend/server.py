from flask import Flask

app = Flask(__name__, static_folder="Frontend")

@app.route('/createqual')
def example():
    print (request.is_json)
    content = request.get_json()
    print (content)
    return 'JSON posted'
    # language = request.args.get('language') #if key doesn't exist, returns None
    # framework = request.args['framework'] #if key doesn't exist, returns a 400, bad request error
    # website = request.args.get('website')

    # return '''<h1>The language value is: {}</h1>
              # <h1>The framework value is: {}</h1>
              # <h1>The website value is: {}'''.format(language, framework, website)

if __name__ == '__main__':
    app.run(port = 5000)
