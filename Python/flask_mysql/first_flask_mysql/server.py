from flask import Flask, request, render_template, redirect, session

from friend import Friend
app = Flask(__name__)

app.secret_key = 'top secret stuff'

@app.route('/')
def index():
    friends = Friend.get_all()
    return render_template("index.html", friends = friends)

@app.route('/create_friend', methods = ["POST"])
def create_friend():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "occupation": request.form["occupation"]
    }
    Friend.save(data)
    return redirect('/')


if __name__=='__main__':
    app.run(debug=True)