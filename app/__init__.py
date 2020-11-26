import os
from flask import Flask
from config import config
from flask_moment import Moment
import os

moment = Moment()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    config[config_name].init_app(app)
    moment.init_app(app)

    prefix = os.getenv('APPLICATION_ROOT') or '/'
    from app.ui import ui as ui_blueprint
    app.register_blueprint(ui_blueprint, url_prefix=prefix)

    from app.api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix=prefix+'/api')

    return app
