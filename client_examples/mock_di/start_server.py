__author__ = 'alexandre'

import os
import logging

from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from mock_di import app

from keys import log_dir

def initialize_logger(output_dir):
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # create error file handler and set level to error
    handler = logging.FileHandler(os.path.join(output_dir, "sands_server.log"), "a", encoding=None, delay="true")
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger


http_server = HTTPServer(WSGIContainer(app))

try:
    port_no = int(app.config['SERVER_NAME'].split(':')[1])
except:
    port_no = 5000

log = initialize_logger(log_dir)
log.info('The process id of this is: ' + str(os.getpid()))
log.info('Starting tornado server on ' + app.config['SERVER_NAME'])

http_server.listen(port_no)

IOLoop.instance().start()