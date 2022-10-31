from flask import Flask, render_template

app = Flask(__name__)

@app.route('/play')
def index():
    return render_template("index.html", num = 3, color = "lightblue")

@app.route('/play/<int:x>')
def num_value(x):
    return render_template("index.html", num = x, color = "lightblue")

@app.route('/play/<int:x>/<color>')
def color_value(x, color):
    return render_template("index.html", num = x, color = color)


if __name__ == "__main__":
    app.run(debug=True)