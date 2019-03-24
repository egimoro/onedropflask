from flask import Flask, render_template,url_for,flash,redirect #render_template enables the html template
                                                #url_for finds exact location of the url

from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
import os

app=Flask(__name__) #the name of the application package

app.config['SECRET_KEY']='88fe5c0981ba01f5b81bcdb8c12dad29'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db' #creates database in the pc location
db=SQLAlchemy(app)
bcrypt=Bcrypt(app)
login_manager=LoginManager(app)
login_manager.login_view='login'
login_manager.login_message_category='info'
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=587
app.config['MAIL_USE_TLS']=True
app.config['MAIL_USERNAME']=os.environ.get('NotifyEmail')
app.config['MAIL_PASSWORD']=os.environ.get('Password')
app.config['ADMINS']=['lopingemma@gmail.com']
mail=Mail(app)

from flaskdrip.users.routes import users
from flaskdrip.posts.routes import posts
from flaskdrip.main.routes import main

app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)

