from flask import Flask, request, render_template, redirect, session

app = Flask(__name__)

app.secret_key = 'keep it safe'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    return redirect('/result')

@app.route('/result')
def result():
    return render_template('form.html', name = session['name'], location = session['location'], 
    language = session['language'], comments = session['comments'])

@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')

if __name__=='__main__':
    app.run(debug=True)