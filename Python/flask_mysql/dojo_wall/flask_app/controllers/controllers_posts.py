from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_app.models.models_user import User
from flask_app.models.models_post import Post

@app.route('/wall')
def success():
    if 'user_id' not in session:
        return redirect('/')
    user_data = {
        'id' : session['user_id']
    }
    user = User.get_one(user_data)
    all = Post.all_posts()
    return render_template('wall.html', user = user, all = all)

@app.route('/create_post', methods=['POST'])
def create_post():
    data = {
        'content' : request.form['content'],
        'user_id' : session['user_id']
    }
    Post.create_post(data)
    return redirect('/wall')