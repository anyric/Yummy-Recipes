from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signin')
def signin():
    return render_template("signin.html")
@app.route('/signup')
def signup():
    return render_template("signup.html")

@app.route('/category')
def category():
    return render_template("category.html")

@app.route('/recipes')
def recipes():
    return render_template("recipes.html")
    
if __name__ ==  '__main__':
    app.run()
    