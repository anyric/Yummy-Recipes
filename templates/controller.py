"""module to controll form data submission"""
from user import User
from modeldb import ModelDB
from category import Category
from recipe import Recipe
from flask import render_template, session, redirect, url_for, request, flash
from run import app

@app.route('/signup', methods=["GET", "POST"])
def signup():
    """method to store usser"""
    if request.method == 'POST':
        customer = User(request.form['name'], request.form['username'], request.form['password'])
        if customer == "Sign Up successful":
            flash(customer, 'info')
            return redirect(url_for('/signin'))
        flash(customer, 'warning')
    return render_template('signup.html')


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    """ Handles the sign_in route """
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username and password:
            if username.strip() and password.strip():
                if ModelDB.ACCOUNTS.get(username):
                    if ModelDB.ACCOUNTS[username].Password == password:
                        session['username'] = request.form['username']
                        return redirect(url_for('/category'))
        return redirect(url_for('/signin'))
    return render_template('signin.html')

@app.route('/category', methods=['GET', 'POST'])
def category():
    """function to store category"""
    if request.method == 'POST':
        cat = Category(request.form['name'], request.form['desc'])
        if cat == "Category added successful":
            flash(cat, 'info')
            return redirect(url_for('/category'))
        flash(cat, 'warning')
    return render_template("category.html")

@app.route('/recipe', methods=['GET', 'POST'])
def recipe():
    """function to store recipe"""
    if request.method == 'POST':
        rec = Recipe(request.form['name'], request.form['desc'])
        if rec == "Recipe added successful":
            flash(rec, 'info')
            return redirect(url_for('/recipe'))
        flash(rec, 'warning')
    return render_template("recipe.html")
