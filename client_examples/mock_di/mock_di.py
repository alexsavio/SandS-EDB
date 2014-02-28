__author__ = 'alexandre&borja'

from sands_client import SandsClient
from forms import RequestForm
import assets

from flask import Flask
from flask import render_template
from flask import request

sands_client = start_sands_client()

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
        recipe = sands_client.ask_for_recipe(form.rq_text.data)
        #request.values['rq_text']
        return str('show_recipe.html', recipe=recipe)

    return render_template('home.html', form=form)


def start_sands_client():
    """

    :return: SandsClient
    SandsClient for DI
    """
    from keys import sands_di_user, sands_di_password, sands_url

    sands_auth = (sands_di_user, sands_di_password)

    req_json_hdrs = {'content-type': 'application/json'}
    req_xml_hdrs = {'content-type': 'application/xml'}

    resp_json_hdrs = {'accept': 'application/json'}
    resp_xml_hdrs  = {'accept': 'application/xml'}

    my_headers = {}
    my_headers.update(req_json_hdrs)
    my_headers.update(resp_json_hdrs)

    return SandsClient(sands_url, sands_auth, my_headers)



if __name__ == "__main__":
     app.run()