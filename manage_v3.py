import typer
import os

app = typer.Typer()

@app.command()
def hello():
    print("no command found")


@app.command()
def createapp(folder):

    if folder == "users":
        path = os.getcwd()
        os.chdir(path)
        n_f = folder
        os.mkdir(n_f)
        p2 = path+'\\'+n_f
        os.chdir(p2)
        f1 = open("forms.py", "w")
        f1.write('''from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from .models import User

#A default RegistrationForm and LoginForm

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username is already in use. Please choose a new username')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email is already in use. Please choose a new email')

class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')''')
        f1.close()
        f2 = open("models.py", "w")
        f2.write('''from main import db

#models here
        
#This is a pre-made user model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(100000), nullable=False)
        
        ''')
        f2.close()
        f3 = open("urls.py", "w")
        f3.write('''from flask import redirect, render_template, url_for, session, request, flash
from main import app, db
from .models import your_models
from .forms import your_forms

#Your routes here


        ''')
    else:
        path = os.getcwd()
        os.chdir(path)
        n_f = folder
        os.mkdir(n_f)
        p2 = path+'\\'+n_f
        os.chdir(p2)
        f1 = open("forms.py", "w")
        f1.write('''from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from .models import User
        
        #Your forms
        ''')
        f1.close()
        f2 = open("models.py", "w")
        f2.write('''from main import db

#models here
        
        
        
        ''')
        f2.close()
        f3 = open("urls.py", "w")
        f3.write('''from flask import redirect, render_template, url_for, session, request, flash
from main import app, db
from .models import your_models
from .forms import your_forms

        #urls here


        ''')

@app.command()
def newproject():
    path = os.getcwd()
    os.chdir(path)
    n_f = "main"
    os.mkdir(n_f)
    rf = open("run_me.py", "w")
    rf.write('''from main import app

if __name__ == '__main__':
    app.run(debug=True)
    ''')
    p2 = path+'\\'+n_f
    os.chdir(p2)
    t_f = "templates"
    os.mkdir(t_f)
    f1 = open("__init__.py", "w")
    f1.write('''from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

app.config["SECRET_KEY"] = "your_secret_key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"

from . import urls

db.create_all()
    ''')
    f1.close()
    f2 = open("urls.py", "w")
    f2.write('''from flask import Flask, redirect, render_template, url_for, session, request, flash
from main import app, db

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():

    return "It worked!"

    ''')
    f2.close()
    p4 = p2 = path+'\\'+n_f+'\\'+"main"+'\\'+"templates"
    os.mkdir(p4)

@app.command()
def create_utils():

    current = os.getcwd()
    path = current+'\\'+"main"
    c = os.chdir(path)

    if path:
        f3 = open("utils.py", "w")
        f3.write('''from . import app, db
from users.models import User
from flask import session

def login_user(uid):
    u = User.query.filter_by(id=int(uid)).first()
    session["logged_in"] = "True"
    session["user_id"] = int(u.id)

def getUserById(id):
    id = int(id)
    u = User.query.filter_by(id=id).first()
    if u:
        return u
    else:
        print("Auth: User with that id is not found")
        return "Auth: User with that id is not found"

def create_user(username, email, password):
    n_u = User(username=username, email=email, password=password)
    db.session.add(n_u)
    db.session.commit()



        ''')
        f3.close()
    else:
        print("PathNotFound: Please create a folder called 'templates' in your main folder. Then rerun this command")

@app.command()
def create_login_template():
    current = os.getcwd()
    path = current+'\\'+"main"+'\\'+"templates"
    c = os.chdir(path)
    if path:
        login_template = open("login.html", "w")
        login_template.write('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>e</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
</head>
<body class="">

    {% with messages = get_flashed_messages(with_categories=true)%}
    {% if messages%}
    {%for category, message in messages %}
      <div class="alert alert-{{ category }} m-3">{{ message }}</div>
    {%endfor %}
    {%endif%}
    {%endwith%}


    <div class="df-form">
      <form method="POST" action="">
          {{ form.hidden_tag() }}
          <fieldset class="df-form m-5">
              <legend class="border-bottom mb-4 text-bold">Log in</legend>

              <div class="form-group mb-3">
              {% if form.email.errors %}
                  {{ form.email(class="form-control is-invalid") }}
                  
                      
                      <div class="invalid-feedback">
                        {% for error in form.email.errors %}
                          <span>{{ error }}</span>
                        {% endfor %}
                      </div>
                      
                  
              {% else %}
                      {{ form.email(class="form-control", placeholder="Email") }}
              {% endif %}

              </div>

              <div class="form-group mb-3">
              {% if form.password.errors %}
                  {{ form.password(class="form-control is-invalid") }}
                  <div class="invalid-feedback">
                    {% for error in form.email.errors %}
                        <span>{{ error }}</span>
                    {% endfor %}
                  </div>
              {% else %}
                      {{ form.password(class="form-control", placeholder="Password") }}
              {% endif %}

              </div>


              {{ form.submit(class="btn btn-primary") }}



              <br>
              <br>

          </fieldset>
          <br>
      </form>
    </div>


</body>
</html>
        ''')
    else:
        print("PathNotFound: Please create a folder called 'templates' in your main folder. Then rerun this command")

if __name__ == '__main__':
    app()