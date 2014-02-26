__author__ = 'alexandre&borja'

from ..sands_client import SandsClient

from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/mock_di")
def mock_di():
    return "Hello World!"

if __name__ == "__main__":
    app.run()