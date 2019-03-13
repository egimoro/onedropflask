from flaskdrip.forms import RegistrationForm,LoginForm
from flask import Flask, render_template,url_for,flash,redirect
from flaskdrip import app,db,bcrypt
from flaskdrip.models import User,Post 
from flask_login import login_user,current_user,logout_user
 
posts=[
     {
          'author':'Gaius Gimoro',
          'title':'test blog 1',
          'content':'First test blog',
          'date_posted':'March 8, 2019'
     },
     {
          'author':'Raius Kimoro',
          'title':'test blog 2',
          'content':'Second test blog',
          'date_posted':'March 8, 2019'   
     }
]

@app.route('/')
@app.route('/home') #@app.route enables functions for routing
def home():
    return render_template('home.html',posts=posts)#variable to have access t the template

@app.route('/about')
def about():
    return render_template('about.html',title='About')

@app.route("/register",methods=['GET','POST'])
def register():
     if current_user.is_authenticated:
          return redirect(url_for('home'))
     form=RegistrationForm()
     if form.validate_on_submit():
         hashed_password=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
         user=User(username=form.username.data,email=form.email.data,password=hashed_password)
         db.session.add(user)
         db.session.commit()
         flash('Your account has been created! You are now able to log in','success')
         return redirect(url_for('login'))

     return render_template('register.html',title='Register',form=form)
     
@app.route("/login",methods=['GET','POST'])
def login():
     if current_user.is_authenticated:
          return redirect(url_for('home'))
     form=LoginForm()
     if form.validate_on_submit():
           user=User.query.filter_by(email=form.email.data).first()
           if user and bcrypt.check_password_hash(user.password,form.password.data):
                login_user(user,remember=form.remember.data)
                return redirect(url_for('home'))
           else:
                flash('Login Unsuccessful. Please check email and password','danger')
     return render_template('login.html',title='Login',form=form)

@app.route('/logout')
def logout():
     logout_user()
     return redirect(url_for('home'))
     
