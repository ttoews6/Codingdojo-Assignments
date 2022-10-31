from flask import Flask, request, render_template, redirect, session
app = Flask(__name__)

app.secret_key = 'keep it a secret, keep it safe'

@app.route('/')
def index():
    if 'counter' not in session:
        session['counter'] = 1
    else: session['counter'] += 1
    return render_template('index.html')

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')


if __name__=='__main__':
    app.run(debug=True)