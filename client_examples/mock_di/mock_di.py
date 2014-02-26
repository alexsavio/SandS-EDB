__author__ = 'alexandre&borja'

from sands_client import SandsClient
from forms import RequestForm
import assets

from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)
app.config.from_pyfile('settings.py')

assets.init_app(app)

@app.route("/")
def home():
    form = RequestForm()
    return render_template('home.html', form=form)

@app.route("/recipe", methods = ['GET', 'POST'])
def recipe():
    form = RequestForm()
    if form.validate_on_submit():
        #request.values['rq_text']
        return str(form.rq_text.data)

    return render_template('home.html', form=form)

#app.run()

if __name__ == "__main__":
     app.run()