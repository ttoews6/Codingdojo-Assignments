from dataclasses import dataclass
from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.models_user import User

@app.route('/')
def index():
    users = User.get_all()
    return render_template('index.html', users = users)

# Add a New User
@app.route('/new_user')
def new_user():
    return render_template('new_user.html')

@app.route('/process', methods = ['POST'])
def create():
    if not User.validate_user(request.form):
        return redirect('/new_user')
    User.create(request.form)
    return redirect('/')


# Edit User Page
@app.route('/edit/<int:user_id>')
def edit_user(user_id):
    data = {
        'id' : user_id
    }
    user = User.get_one(data)
    return render_template('edit_user.html', user = user )

@app.route('/update/<int:user_id>', methods = ['POST'])
def update(user_id):
    data = {
        'id' : user_id,
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email'],
    }
    User.update(data)
    return redirect('/')

#Show User
@app.route('/show/user/<int:user_id>')
def show_user(user_id):
    data = {
        'id' : user_id
    }
    user = User.get_one(data)
    return render_template('show_user.html', user = user)

# Delete User
@app.route('/delete/<int:user_id>/user')
def delete(user_id):
    data = {
        'id' : user_id
    }
    User.delete(data)
    return redirect('/')
