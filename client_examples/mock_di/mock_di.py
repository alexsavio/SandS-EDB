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

@app.route("/", methods = ['GET', 'POST'])
def home():
    rq_form = RequestForm(request.form)
    if request.method == 'POST':
        str(form.rq_text.data)
    return render_template('home.html', form=rq_form)

#app.run()

if __name__ == "__main__":
     app.run()