import os, sqlite3
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from flask import Flask, render_template, url_for, flash, redirect, request
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
    if request.method == 'POST' and form.validate_on_submit():
        conn = get_db_connection()
        cur = conn.cursor()
        nuser = (form.username.data, form.email.data, form.gr_no.data, form.branch.data, form.password.data)
        cur.execute("INSERT INTO suser(sname, gr_no, branch, email, passw) VALUES (?, ?, ?, ?, ?)", nuser)
        conn.commit()
        conn.close()
        flash(f'Account created for {form.username.data}!', 'success') 
        return redirect(url_for('home'))
    return render_template('register.html', title = 'Register', form=form)

@app.route('/login', methods=['GET', 'POST' ])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        conn = get_db_connection()
        users = conn.execute("SELECT * FROM suser WHERE sname = ?",(form.username.data,)).fetchone()
        # print(type(form.username.data))
        # https://fixpython.com/2022/08/fix-python-sqlite3-programmingerror-incorrect-number-of-bindings-supplied-the-current-statement-uses-1-and-there-are-74-supplied-zc1lsif/#:~:text=Now%20we%20will%20see%20solution%20for%20issue%3A%20sqlite3.ProgrammingError%3A,tuple%3A%20cursor.execute%20%28%27INSERT%20INTO%20images%20VALUES%20%28%3F%29%27%2C%20%28img%2C%29%29
        # print(users['branch']) this is working finally
        if users == None:
            flash("duck you! no such user", 'danger')
        else:
            if users['passw'] == form.password.data:
                flash("you've been logged in!", 'success')
                return redirect(url_for('home'))
            else:
                flash('login failed. try again', 'danger')
        
        
    return render_template('login.html', title = 'login', form=form,)

#register page : will write to susers
#login page will verify from susers
#once verified, /user/home: you can choose to buy and sell here so
    #buy page for each item
    #sell page for a user

if __name__ == '__main__':
    app.run(debug=True)