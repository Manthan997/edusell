import os, sqlite3
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

basedir = os.path.abspath(os.path.dirname(__file__))
#__file__ holds the current path (absolute) to the file holding app.py(this program)
app = Flask(__name__)
app.config['SECRET_KEY']='abc'
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')

db=SQLAlchemy(app)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    conn = get_db_connection()
    users = conn.execute("SELECT * FROM suser").fetchall()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    #do something for image addition
    conn.close()
    return render_template('home.html', posts=posts, users=users, title='home')

@app.route('/register', methods=['GET', 'POST' ])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success') 
        return redirect(url_for('home'))
    return render_template('register.html', title = 'Register', form=form)

@app.route('/login', methods=['GET', 'POST' ])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        #the real password data is used here. for now lets make a dummy data point.
        if form.username.data == 'abc' and form.password.data == 'abc':
            flash("you've been logged in!", 'success')
            return redirect(url_for('home'))
        else:
            flash('login failed. try again', 'danger')
    return render_template('login.html', title = 'login', form=form)

#register page : will write to susers
#login page will verify from susers
#once verified, /user/home: you can choose to buy and sell here so
    #buy page for each item
    #sell page for a user

if __name__ == '__main__':
    app.run(debug=True)