from flask import Flask, render_template,url_for,flash,redirect #render_template enables the html template
                                                #url_for finds exact location of the url

from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app=Flask(__name__) #the name of the application package

app.config['SECRET_KEY']='88fe5c0981ba01f5b81bcdb8c12dad29'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db' #creates database in the pc location
db=SQLAlchemy(app)
bcrypt=Bcrypt(app)
login_manager=LoginManager(app)

from flaskdrip import routes
