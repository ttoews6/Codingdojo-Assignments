from flask import Flask, request, render_template, redirect, session
from user import User

app = Flask(__name__)

app.secret_key = "key it safe"

@app.route('/')
def index():
    users = User.get_all()
    return render_template('index.html', users = users)

# Add a New User
@app.route('/new_user')
def new_user():
    return render_template('form.html')

@app.route('/process', methods = ['POST'])
def create():
    User.create(request.form)
    return redirect('/')

if __name__=='__main__':
    app.run(debug=True)