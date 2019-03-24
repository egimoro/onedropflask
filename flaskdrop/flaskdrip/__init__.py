from flask import Flask, render_template,url_for,flash,redirect #render_template enables the html template
                                                #url_for finds exact location of the url

from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskdrip.config import Config




db=SQLAlchemy()
bcrypt=Bcrypt()
login_manager=LoginManager()
login_manager.login_view='users.login'
login_manager.login_message_category='info'
mail=Mail()



def create_app(config_class=Config):
    app=Flask(__name__) #the name of the application package
    app.config.from_object(Config)
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    from flaskdrip.users.routes import users
    from flaskdrip.posts.routes import posts
    from flaskdrip.main.routes import main
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)

    return app


