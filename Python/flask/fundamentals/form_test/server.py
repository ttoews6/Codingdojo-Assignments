from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

app.secret_key = "This is my key, don't tell anyone"

@app.route('/')
def index():
    if 'submitted_forms' not in session:
        session['submitted_forms'] = []
    return render_template("index.html")

@app.route('/submit', methods=['POST'])
def submit():
    # print(request.form)
    # print(request.form['last_name'])
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['email'] = request.form['email']
    session['password'] = request.form['password']
    session['submitted_forms'].append(request.form)
    return redirect('/success')

@app.route('/success')
def success():
    return render_template('form.html', first = session['first_name'], last = session['last_name'], users = session['submitted_forms'])

@app.route('/clear')
def clear(): 
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)