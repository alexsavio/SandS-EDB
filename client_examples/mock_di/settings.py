import socket
import os
# import sys
# basedir = os.path.abspath(os.path.dirname(__file__))
# sys.path.append(os.path.join(basedir))
from keys import localhost_server_name

DEBUG = True

CSRF_ENABLED = True
SECRET_KEY = os.urandom(24)

#References:
#http://python-eve.org/config.html

# # We want to run seamlessly our API both locally and on Heroku, so:
#hn = socket.gethostname()
#if hn == 'gicSands':
#     # Running on local machine. Let's just use the local mongod instance.
#
#     # let's not forget the API entry point
#     SERVER_NAME = localhost_server_name
#     #URL_PREFIX = 'mock_di'
#
#elif hn == 'buccaneer':
#     # Running on local machine. Let's just use the local mongod instance.
#
#     # let's not forget the API entry point
#     SERVER_NAME = localhost_server_name
#     #URL_PREFIX = 'mock_di'




