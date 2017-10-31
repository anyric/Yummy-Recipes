from flask import Flask, render_template

app = Flask(__name__)

@app.route('/Designs')
def dashbaord():
    return render_template("dashboard")

@app.route('/Designs/category')
def category():
    return render_template("category")

@app.route('/Designs/recipes')
def recipes():
    return render_template("recipes")

if __name__ ==  '__main__':
    app.run()