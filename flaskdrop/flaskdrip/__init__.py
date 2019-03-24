from flask import Flask, render_template,url_for,flash,redirect #render_template enables the html template
                                                #url_for finds exact location of the url

from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskdrip.config import Config

app=Flask(__name__) #the name of the application package
app.config.from_object(Config)

db=SQLAlchemy(app)
bcrypt=Bcrypt(app)
login_manager=LoginManager(app)
login_manager.login_view='users.login'
login_manager.login_message_category='info'
mail=Mail(app)

from flaskdrip.users.routes import users
from flaskdrip.posts.routes import posts
from flaskdrip.main.routes import main

app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)

    

