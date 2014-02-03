import socket
import models

#References:
#http://python-eve.org/config.html

# We want to run seamlessly our API both locally and on Heroku, so:
hn = socket.gethostname()
if hn == 'gicSands':
    # Running on local machine. Let's just use the local mongod instance.

    # Please note that MONGO_HOST and MONGO_PORT could very well be left
    # out as they already default to a bare bones local 'mongod' instance.
    MONGO_HOST = 'localhost'
    MONGO_PORT = 27017
    MONGO_USERNAME = 'sands'
    MONGO_PASSWORD = 'unprepared ices false tripping'

    MONGO_DBNAME = 'sands'

    # let's not forget the API entry point
    #SERVER_NAME = '158.227.113.136:8000'
    #SERVER_NAME = 'api.sands-social-network-mockup.com:8000'
    SERVER_NAME = '127.0.0.1:8000'
    URL_PREFIX = 'api'

elif hn == 'buccaneer':
    # Running on local machine. Let's just use the local mongod instance.

    # Please note that MONGO_HOST and MONGO_PORT could very well be left
    # out as they already default to a bare bones local 'mongod' instance.
    MONGO_HOST = 'localhost'
    MONGO_PORT = 27017
    MONGO_USERNAME = 'sands'
    MONGO_PASSWORD = 'unprepared ices false tripping'

    MONGO_DBNAME = 'sands'

    # let's not forget the API entry point
    SERVER_NAME = 'localhost:8000'
    URL_PREFIX = 'api'

elif hn == 'corsair':
    # Running on local machine. Let's just use the local mongod instance.

    # Please note that MONGO_HOST and MONGO_PORT could very well be left
    # out as they already default to a bare bones local 'mongod' instance.
    MONGO_HOST = 'localhost'
    MONGO_PORT = 27017
    MONGO_USERNAME = 'sands2'
    MONGO_PASSWORD = 'unprepared ices false tripping'

    MONGO_DBNAME = 'sands'

    # let's not forget the API entry point
    SERVER_NAME = 'localhost:8000'
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
