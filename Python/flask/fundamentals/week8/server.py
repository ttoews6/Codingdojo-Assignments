from flask import Flask, request, render_template, redirect, session
import random

app = Flask(__name__)

app.secret_key = 'sweet as apple pie'

@app.route('/')
def index():
    if 'adopt' not in session:
        session['adopt'] = 0
    
    return render_template('index.html')

@app.route('/adopt', methods=['POST'])
def adopt():
    if 'cat' == request.form['pet']:
        adoption = random.randint( 15,31 )
        session['adopt'] += adoption
        print("Cat: ", adoption)
        return redirect('/')

    if 'dog' == request.form['pet']:
        adoption = random.randint( 30,46 )
        session['adopt'] += adoption
        print("Dog: ", adoption)
        return redirect('/')

    if 'bird' == request.form['pet']:
        adoption = random.randint( 20,23 )
        session['adopt'] += adoption
        print("Bird: ", adoption)
        return redirect('/')

    if 'donation' == request.form['pet']:
        adoption = random.randint( 15,2000 )
        session['adopt'] += adoption
        print("Donation: ", adoption)
        return redirect('/')

@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')

if __name__=='__main__':
    app.run(debug=True)