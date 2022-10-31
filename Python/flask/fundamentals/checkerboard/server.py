from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/<int:x>/<int:y>')
def rows(x, y):
    return render_template("index.html", num = x, num2 = y)

if __name__ == "__main__":
    app.run(debug=True)