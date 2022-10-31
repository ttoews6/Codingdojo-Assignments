
from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.models_order import Cookie

@app.route('/')
def index():
    cookies = Cookie.get_all()
    return render_template('index.html', cookies = cookies)

@app.route('/new_order')
def new_order():
    return render_template('new_order.html')

@app.route('/process', methods = ['POST'])
def create():
    valid = Cookie.validate_order(request.form)
    if valid:
        Cookie.new_order(request.form)
        return redirect('/')
    return redirect('/new_order')


@app.route('/edit/<int:cookie_id>')
def edit_order( cookie_id ):
    data = {
        'id' : cookie_id
    }
    cookie = Cookie.get_one(data)
    return render_template('edit_order.html' , cookie = cookie)

@app.route('/update/<int:cookie_id>', methods = ['POST'])
def update( cookie_id ):
    data = {
        'id' : cookie_id,
        'first_name' : request.form['first_name'],
        'cookie_type': request.form['cookie_type'],
        'num_boxes' : request.form['num_boxes'],
    }
    Cookie.update(data)
    return redirect('/')