
import os
import logging

from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from eve_api import app

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

log = initialize_logger('/home/gicsands/projects/sands-edb')
log.info('The process id of this is: ' + str(os.getpid()))
log.info('Starting tornado server on ' + app.config['SERVER_NAME'])

http_server.listen(port_no)

IOLoop.instance().start()


# def main():
#     handlers = [
#         (r"/", HomeHandler),
#     ]
#     settings = dict(
#        blog_title=u"Tornado Blog",
#         template_path=os.path.join(os.path.dirname(__file__), "templates"),
#         static_path=os.path.join(os.path.dirname(__file__), "static"),
#         cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
#         debug=True,
#         certfile = os.path.join("certs/server.crt"),
#         keyfile = os.path.join("certs/server.key"),
#         ssl_options = {
#             "certfile" : os.path.join("certs/server.crt"),
#             "keyfile" : os.path.join("certs/server.key"),
#         },
#     )
#     tornado.options.parse_command_line()
#     http_server = tornado.httpserver.HTTPServer(Application())
#     http_server.listen(options.port)
#     tornado.ioloop.IOLoop.instance().start()
#
# main()
