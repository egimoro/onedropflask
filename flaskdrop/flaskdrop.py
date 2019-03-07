from flask import Flask, render_template #render_template enables the html template
app=Flask(__name__) #the name of the application package

posts=[
     {
          'author':'Gaius Gimoro',
          'title':'test blog 1',
          'content':'First test blog',
          'date_posted':'March 8,2019'
     },
     {
          'author':'Raius Kimoro',
          'title':'test blog 2',
          'content':'Second test blog',
          'date_posted':'March 8,2019'   
     }
]

@app.route('/')
@app.route('/home') #@app.route enables functions for routing
def jambo():
    return render_template('home.html',posts=posts)#variable to have access t the template

@app.route('/about')
def about():
    return render_template('about.html')

if __name__=='__main__': #if the name of the app matches the main script jambo
     app.run(debug=True)  #run the app when debugging

