# -*- coding: utf-8 -*-

from flask_assets import Environment, Bundle

#: application css bundle
# css_webapp = Bundle("less/webapp.less",
#                     filters="less", output="css/webapp_less.css",
#                     debug=False)


#: consolidated css bundle
css_bootstrap = Bundle("css/lib/bootstrap/bootstrap.min.css",
                       "css/lib/bootstrap/bootstrap-responsive.min.css",
                       "css/lib/bootstrap/bootstrap-theme.min.css",
                       filters="cssmin", output="css/bootstrap_all.min.css")

css_local = Bundle("css/navbar.css",
                   "css/glyph-inside-input.css",
                   "css/justified-nav.css",
                   "css/sticky-footer-navbar.css",
                   filters="cssmin", output="css/webapp.min.css")

#: vendor js bundle
js_local = Bundle('js/local.js',
                  filters="jsmin", output="js/webapp.min.js")

js_bootstrap = Bundle('js/lib/bootstrap/bootstrap.min.js',
                      filters="jsmin", output="js/bootstrap_all.min.js")


js_angular = Bundle('js/lib/angular/angular.min.js',
                    filters="jsmin", output="js/angular_all.min.js")


js_jquery = Bundle('js/lib/jquery/jquery-2.0.3.min.js',
                   filters="jsmin", output="js/jquery_all.min.js")

#: application js bundle
#js_coffee = Bundle("coffee/.coffee"),
#                   filters="coffeescript", output="js/from_coffee.js")


def init_app(app):
    webassets = Environment(app)

    webassets.register('css_bootstrap', css_bootstrap)
    webassets.register('css_local', css_local)

    webassets.register('js_local', js_local)
    webassets.register('js_jquery', js_jquery)
    webassets.register('js_bootstrap', js_bootstrap)
    webassets.register('js_angular', js_angular)
    #webassets.register('js_coffee', js_coffee)

    webassets.manifest = 'cache' if not app.debug else False
    webassets.cache = not app.debug
    webassets.debug = app.debug
