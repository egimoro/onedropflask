from flask import Flask, render_template,url_for #render_template enables the html template
                                                #url_for finds exact location of the url


from forms import RegistrationForm,LoginForm

app=Flask(__name__) #the name of the application package

app.config['SECRET_KEY']='88fe5c0981ba01f5b81bcdb8c12dad29'

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
def jambo():
    return render_template('home.html',posts=posts)#variable to have access t the template

@app.route('/about')
def about():
    return render_template('about.html',title='About')

@app.route("/register",methods=['GET','POST'])
def register():
     form=RegistrationForm()
     return render_template('register.html',title='Register',form=form)
     
@app.route("/login")
def login():
     form=LoginForm()
     return render_template('login.html',title='Login',form=form)

if __name__=='__main__': #if the name of the app matches the main script jambo
     app.run(debug=True)  #run the app when debugging

