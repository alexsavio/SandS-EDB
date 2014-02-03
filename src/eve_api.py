

import os
import sys
basedir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(basedir))

from keys import *

import bcrypt
from eve import Eve
from eve.io.mongo import Validator

from flask.ext.pymongo import PyMongo
#from flask_sslify import SSLify
from eve.auth import BasicAuth, TokenAuth
#from werkzeug.security import check_password_hash

#mail
#from flask_mail import Mail
#from mail import mail

#eve-docs
from flask.ext.bootstrap import Bootstrap
from eve_docs import eve_docs

#Accounts management:
#http://python-eve.org/tutorials/account_management.html?highlight=objectid

#Bcrypt example:
#http://python-eve.org/authentication.html#basic-authentication-with-bcrypt
class BCryptAuth(BasicAuth):

    def check_auth(self, username, password, allowed_roles, resource, method):
        print(resource)
        if resource == 'account':
            return username == 'sands' and password == sands_password
        else:
            # use Eve's own db driver; no additional connections/resources are used
            accounts = app.data.driver.db['account']

            lookup = {'username': username}
            if allowed_roles:
                # only retrieve a user if his roles match ``allowed_roles``
                lookup['roles'] = {'$in': allowed_roles}

            account = accounts.find_one(lookup)

            #User-Restricted Resource Access
            # set 'auth_field' value to the account's ObjectId
            # (instead of _id, you might want to use ID_FIELD)
            #if account and '_id' in account:
            #    self.request_auth_value = account['_id']

            return account \
                and bcrypt.checkpw(password, account['password'])


class SandsValidator(Validator):

    def _validate_type_daydate(self, field, value):
        """
        Enables validation for `daydate` schema attribute.
        :param field: field name.
        :param value: field value.
        """
        from time import strptime

        try:
            strptime(value, "%d/%m/%Y")
        except ValueError as e:
            self._error(field, ERROR_BAD_TYPE % 'daydate (format: DD/MM/YYYY)')


    def _validate_type_dayhour(self, field, value):
        """
        Enables validation for `dayhour` schema attribute.
        :param field: field name.
        :param value: field value.
        """
        from time import strptime

        try:
            strptime(value, "%H:%M:%S")
        except ValueError as e:
            self._error(field, ERROR_BAD_TYPE % 'dayhour (format: H:M:S)')


app = Eve(auth=BCryptAuth, validator=SandsValidator, settings='settings.py')

#eve-docs
bootstrap = Bootstrap(app)
app.register_blueprint(eve_docs, url_prefix='/docs')

#app.debug = True


@app.before_first_request
def create_roles():
    account = app.data.driver.db['account']

    account.insert({'username': 'sands',
                    'password': sands_password1_hash,
                    'roles': ['superuser']})

    account.insert({'username': 'sands_ni',
                    'password': sands_ni_password_hash,
                    'roles': ['admin']})

    account.insert({'username': 'sands_di',
                    'password': sands_di_password_hash,
                    'roles': ['admin']})

#SSLify
#sslify = SSLify(app)#, permanent=True, subdomains=True)

#mail
#app.config.update(mail)
#appmail = Mail(app)

#user_datastore = EveUserDatastore(app, 'account', 'account_role')
#security = Security(app, user_datastore)

# Create a user to test with
#@app.before_first_request
#def create_user():
#    user_datastore.create_user(email='alexsavio@gmail.com', password='password')

if __name__ == '__main__':
    app.run()

