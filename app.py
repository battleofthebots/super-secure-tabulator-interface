from flask import Flask, render_template_string, request
from os import *
from jinja2 import exceptions
app = Flask(__name__)

@app.route('/')
def index():
    template = '''
    <!DOCKTYPE html>
    <html>
    <head>
    <style>
    body{font-size: 1.5em;}
    input { width: 100%;padding: 12px 20px; }
    h1 { text-align: center; padding: 20px; font-size: 2.5em; }
    </style>
    </head>
    <body>
    <h1> Calculator app
    </h1>
    Use our state of the art tabulator! Recognized operations include:
    <ul>
    <li>Addition with +</li>
    <li>Subtraction with -</li>
    <li>Multiplication with *</li>
    <li>Division with /</li>
    <li><b>Other operations are untested</b></li>
    </ul>
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
    app.run(host='0.0.0.0', port=8080)