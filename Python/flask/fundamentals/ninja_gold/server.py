from flask import Flask, request, render_template, redirect, session

import random

from datetime import datetime

app = Flask(__name__)

app.secret_key = 'keep it safe'

now = datetime.now()

date_time = now.strftime("(%Y-%m-%d %H:%M:%S)")

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
    if 'activity' not in session:
        session['activity'] = []
    if 'datetime' not in session:
        session['datetime'] = 0
    if 'money' not in session:
        session['money'] = 0
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
    if 'farm' == request.form['ninja_gold']:
        money = random.randint(10,20)
        session['gold'] += money
        session['activity'].append(f"Earned {money} golds from the farm! {date_time}")
        session['money'] = money
        return redirect('/')
    
    if 'cave' == request.form['ninja_gold']:
        money = random.randint(5,10)
        session['gold'] += money
        session['activity'].append(f"Earned {money} golds from the cave! {date_time}")
        session['money'] = money
        return redirect('/')

    if 'house' == request.form['ninja_gold']:
        money = random.randint(2,5)
        session['gold'] += money
        session['activity'].append(f"Earned {money} golds from the house! {date_time}")
        session['money'] = money
        return redirect('/')

    if 'casino' == request.form['ninja_gold']:
        money = random.randint(-50,50)
        session['gold'] += money
        session['money'] = money
        if money < 0:
            session['activity'].append(f"Entered a casino and lost {money} golds... Ouch.. {date_time}")
            print(f"Entered a casino and lost {money} golds... Ouch..")
        elif money > 0:
            session['activity'].append(f"Entered a casino and won {money} golds... Awesome! {date_time}")
            print(f"Entered a casino and won {money} golds... Aweome!")
        return redirect('/')


@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')


if __name__=='__main__':
    app.run(debug=True)