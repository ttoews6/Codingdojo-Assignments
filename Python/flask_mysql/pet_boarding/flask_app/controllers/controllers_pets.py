from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_app.models.models_user import User
from flask_app.models.models_pet import Pet

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    user_data = {
        'id' : session['user_id']
    }
    user = User.get_one(user_data)
    all = Pet.get_all_who_liked()
    return render_template('dashboard.html', user = user, all = all)

#Adding a pet page
@app.route('/add_pet')
def add_pet():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('new_pet.html')

#Create a Pet
@app.route('/create_pet', methods=['POST'])
def create_pet():
    data = {
        'name' : request.form['name'],
        'breed' : request.form['breed'],
        'dob' : request.form['dob'],
        'gender' : request.form['gender'],
        'hair_color' : request.form['hair_color'],
        'information' : request.form['information'],
        'user_id' : session['user_id']
    }
    Pet.create_pet(data)
    return redirect('/dashboard')

#Edit Page
@app.route('/edit_pet/<int:pet_id>')
def edit_pet(pet_id):
    data = {
        'id' : pet_id
    }
    pet = Pet.get_one(data)
    return render_template('edit_pet.html', pet = pet)

#Update Pet
@app.route('/update_pet/<int:pet_id>', methods=['POST'])
def update_pet(pet_id):
    Pet.update_pet(request.form, pet_id)
    return redirect('/dashboard')

#Show Pet
@app.route('/one_pet/<int:pet_id>')
def show_pet(pet_id):
    data = {
        'id' : pet_id
    }
    pet = Pet.get_one(data)
    return render_template('one_pet.html', pet = pet)

#Like and Dislike Pet
@app.route('/like/<int:pet_id>')
def like(pet_id):
    data = {
        'pet_id' : pet_id,
        'user_id' : session['user_id']
    }
    Pet.like(data)
    return redirect('/dashboard')

@app.route('/dislike/<int:pet_id>')
def dislike(pet_id):
    data = {
        'pet_id' : pet_id,
        'user_id' : session['user_id']
    }
    Pet.dislike(data)
    return redirect('/dashboard')

#Delete Pet
@app.route('/delete_pet/<int:pet_id>')
def delete_pet(pet_id):
    data = {
        'id' : pet_id
    }
    Pet.delete_pet(data)
    return redirect('/dashboard')
