import os

class Config:
    SECRET_KEY=os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI=os.environ.get('SQLALCHEMY_DATABASE_URI') #creates database in the pc location
    MAIL_SERVER ='smtp.gmail.com'
    MAIL_PORT=587
    MAIL_USE_TLS=True
    MAIL_USERNAME=os.environ.get('NotifyEmail')
    MAIL_PASSWORD=os.environ.get('Password')
    ADMINS=os.environ.get('ADMINS')