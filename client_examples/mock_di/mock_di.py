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


def start_sands_client():
    from keys import sands_di_user, sands_di_password

    from sands_client import SandsClient

    #sands_url = 'http://localhost:5000/api/'
    #SERVER_NAME = '158.227.113.136:8080'
    #SERVER_NAME = 'api.sands-social-network-mockup.com:8080'

    sands_url = 'http://api.sands-social-network-mockup.com:8080/api/'

    sands_auth = (sands_user, sands_password1)

    req_json_hdrs = {'content-type': 'application/json'}
    req_xml_hdrs = {'content-type': 'application/xml'}

    resp_json_hdrs = {'accept': 'application/json'}
    resp_xml_hdrs  = {'accept': 'application/xml'}

    my_headers = {}
    my_headers.update(req_json_hdrs)
    my_headers.update(resp_json_hdrs)

    #r = requests.get(sands_url + 'Evaluation', auth=sands_auth, headers=my_headers)


    #Sands Client
    sands_client = SandsClient(sands_url, sands_auth, my_headers)
#app.run()

if __name__ == "__main__":
     app.run()