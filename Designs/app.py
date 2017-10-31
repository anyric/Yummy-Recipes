from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def dashbaord():
    return render_template("index.html")

@app.route('/category')
def category():
    return render_template("category")

@app.route('/recipes')
def recipes():
    return render_template("recipes")

if __name__ ==  '__main__':
    app.run()
    