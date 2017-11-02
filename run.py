""" module that initiates flask app"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """function to display home page"""
    return render_template('index.html')


@app.route('/signup')
def signup():
    """function to display signup page"""
    return render_template("signup.html")

@app.route('/signin')
def signin():
    """function to display signin page"""
    return render_template("signin.html")

@app.route('/category')
def category():
    """function to display category page"""
    return render_template("category.html")

@app.route('/recipes')
def recipes():
    """function to display recipes page"""
    return render_template("recipes.html")

if __name__ == '__main__':
    app.run()
