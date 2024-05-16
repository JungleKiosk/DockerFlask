from flask import Flask, render_template, request, url_for, redirect
from os import environ
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
    user=environ.get('POSTGRES_USER'),
    pw=environ.get('POSTGRES_PASSWORD'),
    url=environ.get('POSTGRES_URL'),
    db=environ.get('POSTGRES_DB')
)

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL

db = SQLAlchemy(app)

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    surname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __init__(self, name, surname, email, password):
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('home/home.html')

@app.route('/login')
def login():
    return render_template('home/user/login.html', page='login')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
        
        if request.method == 'POST':
            name = request.form['name']
            surname = request.form['surname']
            email = request.form['email']
            password = request.form['password']

            new_user = Users(name=name, surname=surname, email=email, password=password)
            db.session.add(new_user)
            db.session.commit()

            return redirect(url_for('home'))

        return render_template('home/user/signup.html', page='signup')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=environ.get('PORT'), debug=environ.get('DEBUG'))