from flask import render_template
from core import app
@app.route('/')
def index():
    greeting="Hello World!"
    return render_template('index.html', greet=greeting)