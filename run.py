""" module that initiates flask app"""
import os
from utilities.user import User
from utilities.modeldb import ModelDB
from utilities.category import Category
from utilities.recipe import Recipe
from flask import Flask, render_template, redirect, url_for, request#, flash, Session

app = Flask(__name__)
#app.config['SESSION_TYPE'] = 'memcached'
#app.config['SECRET_KEY'] = 'super secret key'
#sess = Session()
user_dict = {}
model = ModelDB()
user_obj = None


@app.route('/')
def index():
    """function to display home page"""
    return render_template('index.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """function to display signup page and redirect to sigin page"""
    global user_obj
    if request.method == 'POST':
        name = request.form['name']
        username = request.form['username']
        password = request.form['password']
        
        user_obj = User(name, username, password)
        user_dict[username] = user_obj

        if user_obj.adduser():
            model.ACCOUNTS[username] = user_obj.adduser()
            return redirect(url_for('signin'))
    return render_template("signup.html")


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    """ Handles the sign_in route """
    global user_obj
   
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username.strip() and password.strip():
            if user_obj.verifyuser(username, password, model.ACCOUNTS):
                return redirect(url_for('category'))
    return render_template("signin.html")


@app.route('/categorylist', methods=['GET', 'POST'])
def categorylist():
    """function to store category"""
    if request.method == 'POST':
        name = request.form['name']
        desc = request.form['desc']

        cat = Category(name, desc)
        model.CATDATA[name] = cat
        return redirect(url_for('categorylist'))
    return render_template("categorylist.html")

@app.route('/category')
def category():
    """function to store category"""
    cate = model.CATDATA

    num = len(cate)
    if num > 0:
        return render_template("category.html", cate=cate)
    return render_template("category.html")


@app.route('/recipelist', methods=['GET', 'POST'])
def recipelist():
    """function to store recipe"""
    if request.method == 'POST':
        name = request.form['name']
        desc = request.form['desc']

        rec = Recipe(name, desc)
        model.RECDATA[name] = rec
        return redirect(url_for('recipelist'))
    return render_template("recipelist.html")


@app.route('/recipe', methods=['GET', 'POST'])
def recipe():
    """function to store recipe"""
    rec = model.RECDATA

    num = len(rec)
    if num > 0:
        return render_template("recipes.html", rec=rec)
    return render_template("recipes.html")


@app.before_request
def before_request():
    """"""
if __name__ == '__main__':
    app.debug = True
    #port = int(os.environ.get('PORT', 5000))
    app.config['SESSION_TYPE'] = 'file_system'
    app.config['SECRET_KEY'] = 'redsfsfsfsfis'

    #app.run(host='0.0.0.0', port = port)
    app.run()
