from flaskdrip import create_app

app=create_app()

if __name__=='__main__': #if the name of the app matches the main script jambo
     app.run(debug=True)  #run the app when debugging


