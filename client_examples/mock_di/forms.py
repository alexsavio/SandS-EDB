__author__ = 'alexandre'

from flask.ext.wtf import Form
from wtforms import TextField, BooleanField
from wtforms.validators import Required

class RequestForm(Form):
    rq_text = TextField('request', validators=[Required()])