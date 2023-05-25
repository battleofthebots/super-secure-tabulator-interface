from flask import Flask, render_template_string, request
from os import *
from jinja2 import exceptions
app = Flask(__name__)

@app.route('/')
def index():
    template = '''
    <!DOCKTYPE html>
    <html>
    <body>
    <h1> Calculator app
    </h1>
    Make sure to use proper syntax!
    <form action="/result" method="get">
    <input type="text" id="equation" name="equation">
    <input type="submit" value="Submit">
    </form>
    </body>
    </html>
    '''
    return render_template_string(template)

@app.route('/result', methods=['GET'])
def result():
    equation = request.args.get('equation')
    return render_template_string("{{" + equation + "}}")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)