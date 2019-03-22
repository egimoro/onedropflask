from flask import Blueprint,request,render_template
from flaskdrip.models import Post
main=Blueprint('main',__name__)

@main.route('/')
@main.route('/home') #@main.route enables functions for routing
def home():
     page=request.args.get('page',1,type=int)
     posts=Post.query.order_by(Post.date_posted.desc()).paginate(page=page,per_page=1)
     return render_template('home.html',posts=posts)#variable to have access t the template

@main.route('/about')
def about():
    return render_template('about.html',title='About')