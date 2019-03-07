""" This is a project following the tutorial of flask.pocoo.org"""

import os

from flask import Flask

def create_app(test_config=None):
    # create and configure the app
    app=Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='kazibure',
        DATABASE=os.path.join(app.instance_path,'flaskdrop.sqlite')
        
    )

    if test_config is None:
        # load the instance config, if it exists, whwn not testing
        app.config.from_pyfile('config.py',silent=True)
    else:
        #Load the config if passed in
        app.config.from_mapping(test_config)
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says jambo
    @app.route('/')
    @app.route('/jambo')
    def jambo():
        return 'Jambo, World again...?'

    return app
