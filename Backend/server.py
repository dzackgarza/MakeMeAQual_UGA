from flask import Flask

app = Flask(__name__)

@app.route('/createqual')
def example():
   return '{"name":"Bob"}'

if __name__ == '__main__':
    app.run(port = 5000)
