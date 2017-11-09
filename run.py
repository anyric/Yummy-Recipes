""" module that initiates flask app"""
import os
from utilities.user import User
from utilities.modeldb import ModelDB
from utilities.category import Category
from utilities.recipe import Recipe
from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)
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
    return render_template("index.html")


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


@app.route('/categorylist', methods=['GET'])
def getcategorylist():
    """function to get category page"""
    return render_template("categorylist.html")


@app.route('/categorylistpost', methods=['POST'])
def categorylistpost():
    """function to store category"""

    name = request.form['name']
    desc = request.form['desc']
    categoryobject = Category(name, desc)
    model.CATDATA[name] = categoryobject.addcategory()

    return redirect(url_for('category'))
    
@app.route('/category')
def category():
    """function to store category"""
    viewcategory = model.CATDATA
    
    #num = len(category)
    #if num > 0:
    return render_template("category.html", viewcategory=viewcategory)
    #return render_template("category.html")


@app.route('/delcatetgory/<name>')
def delcatetgory(name):
    """function to store category"""
    deletecategory = model.CATDATA

    num = len(deletecategory)
    if num > 0:
        model.CATDATA.pop(name)
        deletecategory = model.CATDATA

        return render_template("category.html", deletecategory=deletecategory)
    return render_template("category.html")


@app.route('/editcatetgory/<name>')
def editcatetgory(name):
    """function to store category"""
    deletecategory = model.CATDATA

    num = len(deletecategory)
    if num > 0:
        model.CATDATA.pop(name)
        deletecategory = model.CATDATA

        return render_template("category.html", deletecategory=deletecategory)
    return render_template("category.html")


@app.route('/getcatetgory')
def getcatetgory():
    """function to store category"""
    getcategory = model.CATDATA

    num = len(getcategory)
    if num > 0:
        return render_template("recipelist.html", getcategory=getcategory)
    return render_template("category.html")

@app.route('/recipelist', methods=['GET', 'POST'])
def recipelist():
    """function to store recipe"""
    if request.method == 'POST':
        categ = request.form['category']
        name = request.form['name']
        desc = request.form['desc']

        rec = Recipe(categ, name, desc)

        model.RECDATA[name] = rec.addrecipe()
        return redirect(url_for('recipe'))
    return render_template("recipelist.html")


@app.route('/recipe', methods=['GET', 'POST'])
def recipe():
    """function to display recipe"""
    rec = model.RECDATA

    num = len(rec)
    if num > 0:
        return render_template("recipes.html", rec=rec)
    return render_template("recipes.html")


@app.route('/delrecipe/<name>')
def delrecipe(name):
    """function to del recipe"""
    rec = model.CATDATA

    num = len(rec)
    if num > 0:
        model.RECDATA.pop(name)
        rec = model.RECDATA

        return render_template("recipe.html", rec=rec)
    return render_template("recipe.html")

if __name__ == '__main__':
    app.debug = True
    
    app.config['SESSION_TYPE'] = 'file_system'
    app.config['SECRET_KEY'] = 'redsfsfsfsfis'

    
    app.run()
