from flask import Response, render_template, request, url_for
from app import app


@app.route('/', methods=['GET'])
def index():
    context = {}
    return render_template('index.html', context=context)
