from flask import Blueprint, render_template, url_for

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')  #"it is main page"

@auth.route('/register')
def register():
    return render_template('register.html') #"Home Page"

@auth.route('/logout')
def logout():
    return "new"