from datetime import datetime
from flask import Flask
from flask import render_template
from flask import url_for
from flask import flash
from flask import redirect
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy

#import secrets
app = Flask(__name__)
app.config['SECRET_KEY'] = 'a9705bdad25a1836d4c5d849dd028ecb'
# print(secrets.token_hex(16))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User({self.username}, {self.email}, {self.image_file}, {self.password})"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post({self.title}, {self.date_posted})"


posts = [
    {
        'author': 'Pranoto Budi',
        'title': 'Title 1',
        'content': "Content 1",
        'date_posted': 'August 10, 2018',
    },
    {
        'author': 'Dwi Hendro',
        'title': 'Title 2',
        'content': "Content 2",
        'date_posted': 'August 11, 2018',
    },
]


@app.route("/")
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@gmail.com' and form.password.data == 'password':
            flash(f'You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash(f'Login unsuccessful. Please check your username and password', 'danger')

    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
