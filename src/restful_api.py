__author__ = 'alexandre'

from flask import Flask
from pymongo import ObjectId
from flask.ext.mongoengine import MongoEngine, MongoEngineSessionInterface
import mongoapi_config

import ujson
from datetime import datetime

#from mongoengine import connect
#connect('sands')
#connect('sands', username='alexandre', password='bottles beaches modified persuasive')

app = Flask(__name__)
app.config.from_object(mongoapi_config.TestingConfig)
db = MongoEngine(app)

app.session_interface = MongoEngineSessionInterface(db)

mime_types = {'json_renderer': ('application/json',),
              'xml_renderer': ('application/xml', 'text/xml',
                               'application/x-xml',)}

@app.route('/<regex("[\w]*[Ss]"):collection>')
def collection(collection):
    if collection in


@app.route('/<regex("[\w]*[Ss]"):collection>/<lookup>')
@app.route('/<regex("[\w]*[Ss]"):collection>'
           '/<regex("[a-f0-9]{24}"):object_id>')
def document(collection, lookup=None, object_id=None):



class APIEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return datetime.strptime(obj, '%Y%m%d')
        elif isinstance(ob, ObjectId):
            return str(obj)
        return json.JSONEncoder.default(self, obj)


def json_renderer(**data):
    return ujson.dumps(data, cls=APIEncoder)


def prep_response(dct, status=200):
    mime, render = get_best_mime()
    rendered = globals()[render](**dct)
    resp = make_response(rendered, status)


class RegexConverter(BaseConverter)

if __name__ == '__main__':
    app.run()


