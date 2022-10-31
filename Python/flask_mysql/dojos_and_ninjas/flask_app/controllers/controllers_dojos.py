from flask_app import app
from flask import render_template, redirect, request
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.models_dojo import Dojo
from flask_app.models.models_ninja import Ninja

@app.route('/')
def index():
    dojos = Dojo.get_all()
    return render_template('index.html', dojos = dojos)

# Add a Dojo
@app.route('/create_dojo', methods = ['POST'])
def create_dojo():
    Dojo.create_dojo(request.form)
    return redirect('/')

# Show Dojo
@app.route('/show_dojo/<int:dojo_id>')
def show_dojo(dojo_id):
    data = {
        'id' : dojo_id
    }
    dojo = Dojo.show_dojo(data)
    ninjas = Ninja.ninjas_and_dojos(data)
    return render_template('show_dojo.html', dojo = dojo, ninjas = ninjas)

