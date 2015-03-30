""" Views redirecting to the appropriate HTML file content. (Flask Routes) """

from flask_templates import app
from flask import render_template


@app.route('/index')
@app.route('/')
def index():
    """Main page of the website."""
    return render_template('index.html')
    pass
