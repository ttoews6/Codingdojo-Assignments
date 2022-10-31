from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_app.models.models_user import User
from flask_app.models.models_recipe import Recipe

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    user_data = {
        'id' : session['user_id']
    }
    user = User.get_one(user_data)
    all = Recipe.all_recipes()
    return render_template('dashboard.html', user = user, all = all)

@app.route('/add_recipe')
def add_recipe():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('create_recipe.html')


@app.route('/create_recipe', methods=['POST'])
def create_recipe():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'name' : request.form['name'],
        'description' : request.form['description'],
        'instructions' : request.form['instructions'],
        'date_made' : request.form['date_made'],
        'under' : request.form['under'],
        'user_id' : session['user_id'],
    }
    valid = Recipe.recipe_validator(data)
    if valid:
        Recipe.create_recipe(data)
        return redirect('/dashboard')
    return redirect('/add_recipe')

#View Recipe
@app.route('/view_recipe/<int:recipe_id>')
def view_recipe(recipe_id):
    if 'user_id' not in session:
            return redirect('/')
    data = {
        'id' : recipe_id
    }
    user_data = {
        'id' : session['user_id']
    }
    user = User.get_one(user_data)
    recipe = Recipe.get_one(data)
    return render_template('view_recipe.html', recipe = recipe, user = user)

#Edit Recipe
@app.route('/edit_recipe/<int:recipe_id>')
def edit_recipe(recipe_id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id' : recipe_id
    }
    recipe = Recipe.get_one(data)
    return render_template('edit_recipe.html', recipe = recipe)

#Update Recipe
@app.route('/update_recipe/<int:recipe_id>', methods=['POST'])
def update_recipe(recipe_id):
    Recipe.update_recipe(request.form, recipe_id)
    return redirect('/dashboard')

#Delete Recipe
@app.route('/delete_recipe/<int:recipe_id>')
def delete_recipe(recipe_id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id' : recipe_id
    }
    Recipe.delete_recipe(data)
    return redirect('/dashboard')