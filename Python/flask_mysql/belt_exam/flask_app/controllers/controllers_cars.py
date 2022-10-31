from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_app.models.models_user import User
from flask_app.models.models_car import Car


@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    user_data = {
        'id' : session['user_id']
    }
    user = User.get_one(user_data)
    all = Car.all_cars()
    return render_template('dashboard.html', user = user, all = all)

#add Car
@app.route('/add_car')
def add_car():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('add_car.html')

@app.route('/create_car', methods=['POST'])
def create_car():
    data = {
        'price' : request.form['price'],
        'model' : request.form['model'],
        'make' : request.form['make'],
        'year' : request.form['year'],
        'description' : request.form['description'],
        'user_id' : session['user_id']
    }
    valid = Car.car_validator(data)
    if valid:
        Car.create_car(data)
        return redirect('/dashboard')
    return redirect('/add_car')

#Edit Car
@app.route('/edit_car/<int:car_id>')
def edit_car(car_id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id' : car_id
    }
    car = Car.get_one(data)
    return render_template('edit_car.html', car = car)

#Update Car
@app.route('/update_car/<int:car_id>', methods=['POST'])
def update_car(car_id):
    if 'user_id' not in session:
        return redirect('/')
    Car.update_car(request.form, car_id)
    return redirect('/dashboard')

#View Car
@app.route('/view_car/<int:car_id>')
def view_car(car_id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id' : car_id
    }
    user_data = {
        'id' : session['user_id']
    }
    user = User.get_one(user_data)
    car = Car.get_one(data)
    return render_template('view_car.html', user = user, car = car)

#Delete Car
@app.route('/delete_car/<int:car_id>')
def delete_car(car_id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id' : car_id
    }
    Car.delete_car(data)
    return redirect('/dashboard')

