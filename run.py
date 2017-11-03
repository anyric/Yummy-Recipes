""" module that initiates flask app"""
#from utilities.user import User
#from utilities.modeldb import ModelDB
#from utilities.category import Category
#from utilities.recipe import Recipe
from flask import Flask, render_template, redirect, url_for, request#, flash, Session

app = Flask(__name__)
#app.config['SESSION_TYPE'] = 'memcached'
#app.config['SECRET_KEY'] = 'super secret key'
#sess = Session()



app.config['SESSION_TYPE'] = 'memcached'
app.config['SECRET_KEY'] = 'redsfsfsfsfis'


@app.route('/')
def index():
    """function to display home page"""
    return render_template('index.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """function to display signup page"""
    if request.method == 'POST':
        #customer = User(request.form['name'], request.form['username'], request.form['password'])
        #if customer.adduser() == "Sign Up successful":
        name = request.form['name']
        username = request.form['username']
        password = request.form['password']

        print(name + " " + username + " " + password)
        return redirect(url_for('signin'))
    return render_template("signup.html")


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    """ Handles the sign_in route """
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        #if username and password:
        #if username.strip() and password.strip():
        #if ModelDB.ACCOUNTS.get(username):
        #if ModelDB.ACCOUNTS[username].Password == password:
        #                return redirect(url_for('category'))

        print(username + " " + password)
        return redirect(url_for('category'))
    return render_template("signin.html")


@app.route('/categorylist', methods=['GET', 'POST'])
def categorylist():
    """function to store category"""
    if request.method == 'POST':
        #cat = Category(request.form['name'], request.form['desc'])
        #if cat.addcategory() == "Category added successful":

        return redirect(url_for('categorylist'))
    return render_template("categorylist.html")

@app.route('/category', methods=['GET', 'POST'])
def category():
    """function to store category"""
    if request.method == 'POST':
        #cat = Category(request.form['name'], request.form['desc'])
        #if cat.addcategory() == "Category added successful":

        return redirect(url_for('categorylist'))
    return render_template("category.html")


@app.route('/recipe', methods=['GET', 'POST'])
def recipe():
    """function to store recipe"""
    if request.method == 'POST':
        #rec = Recipe(request.form['name'], request.form['desc'])
        #if rec.addrecipe() == "Recipe added successful":
        return redirect(url_for('recipe'))
    return render_template("recipes.html")

if __name__ == '__main__':
    #app.debug = True
    app.run()
