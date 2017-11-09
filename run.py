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
            return redirect(url_for('category'))
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

    return render_template("category.html", viewcategory=viewcategory)


@app.route('/deletecatetgory/<categoryname>')
def delcatetgory(categoryname):
    """function to store category"""

    model.CATDATA.pop(categoryname)

    return redirect(url_for('category'))


@app.route('/editcatetgory/<name>', methods=['POST'])
def editcatetgory(name):
    """function to store category"""
    return name
    old_name = request.form["oldname"]
    new_name = request.form["newname"]
    description = request.form["desc"]

    categorydata = model.CATDATA

    num = len(categorydata)
    if num > 0:
        model.CATDATA.pop(old_name)
        categoryobject = Category(new_name, description)

        model.CATDATA[new_name] = categoryobject
        categorydata = model.CATDATA

        return render_template("category.html", categorydata=categorydata)
    return render_template("category.html")


@app.route('/getcatetgory')
def getcatetgory():
    """function to store category"""
    getcategory = model.CATDATA

    num = len(getcategory)
    if num > 0:
        return render_template("recipelist.html", getcategory=getcategory)
    return render_template("category.html")

@app.route('/recipelistpost', methods=['POST'])
def recipelist():
    """function to store recipe"""
    return request.form['category'] + " " +request.form['name'] + " "+request.form['desc']
    if request.method == 'POST':
        categ = request.form['category']
        name = request.form['name']
        desc = request.form['desc']

        rec = Recipe(categ, name, desc)

        model.RECDATA[name] = rec.addrecipe()
    return redirect(url_for('recipe'))



@app.route('/recipe', methods=['GET', 'POST'])
def recipe():
    """function to display recipe"""
    viewrecipe = model.RECDATA

    return render_template("recipes.html", viewrecipe=viewrecipe)


@app.route('/deleterecipe/<recipename>')
def deleterecipe(recipename):
    """function to delete recipe"""

    model.RECDATA.pop(recipename)

    return redirect(url_for('recipe'))


if __name__ == '__main__':
    app.debug = True
    
    app.config['SESSION_TYPE'] = 'file_system'
    app.config['SECRET_KEY'] = 'redsfsfsfsfis'

    
    app.run()
