import socket
import models

import os
import sys
basedir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(basedir))

from keys import *

#References:
#http://python-eve.org/config.html

# We want to run seamlessly our API both locally and on Heroku, so:
hn = socket.gethostname()
if hn == 'gicSands':
    # Running on local machine. Let's just use the local mongod instance.

    # Please note that MONGO_HOST and MONGO_PORT could very well be left
    # out as they already default to a bare bones local 'mongod' instance.
    MONGO_HOST = mongo_host
    MONGO_PORT = 27017
    MONGO_USERNAME = mongo_user
    MONGO_PASSWORD = mongo_password

    MONGO_DBNAME = mongo_sands_db

    # let's not forget the API entry point
    SERVER_NAME = localhost_server_name
    URL_PREFIX = 'api'

elif hn == 'buccaneer':
    # Running on local machine. Let's just use the local mongod instance.

    # Please note that MONGO_HOST and MONGO_PORT could very well be left
    # out as they already default to a bare bones local 'mongod' instance.
    MONGO_HOST = mongo_host
    MONGO_PORT = 27017
    MONGO_USERNAME = mongo_user
    MONGO_PASSWORD = mongo_password

    MONGO_DBNAME = mongo_sands_db

    # let's not forget the API entry point
    SERVER_NAME = localhost_server_name
    URL_PREFIX = 'api'

elif hn == 'corsair':
    # Running on local machine. Let's just use the local mongod instance.

    # Please note that MONGO_HOST and MONGO_PORT could very well be left
    # out as they already default to a bare bones local 'mongod' instance.
    MONGO_HOST = mongo_host
    MONGO_PORT = 27017
    MONGO_USERNAME = mongo_user
    MONGO_PASSWORD = mongo_password

    MONGO_DBNAME = mongo_sands_db

    # let's not forget the API entry point
    SERVER_NAME = localhost_server_name
    URL_PREFIX = 'api'


#http://python-eve.org/features.html#hateoas-feature
HATEOAS = False

ALLOWED_ROLES = ['superuser', 'admin']

# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

# Enable reads (GET), edits (PATCH), replacements (PUT) and deletes of
# individual items  (defaults to read-only item access).
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

DOMAIN = models.DOMAIN
