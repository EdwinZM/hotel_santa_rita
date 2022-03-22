from wsgiref.validate import validator
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from wtforms import Form, FileField, TextField, DateField, validators
from flask_login import LoginManager, UserMixin, login_user, current_user
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager()
login_manager.init_app(app)

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    img_file = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String, unique=True, nullable=False)
    description = db.Column(db.String, nullable=False)
    date = db.Column(db.String, nullable=False)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String, nullable=False)

db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return user_id

class EventForm(Form):
    name = TextField("Nombre", [validators.DataRequired()])
    description = TextField("Descripción", [validators.DataRequired()])
    date = TextField("Fecha", [validators.DataRequired()])
    image = FileField("Imagen", validators=[validators.DataRequired()])

@app.route("/") 
def home():
    return render_template("index.html")

@app.route("/rooms")
def rooms():
    return render_template("rooms.html")

@app.route("/restaurant")
def restaurant():
    return render_template("restaurant.html")

@app.route("/blog")
def blog():
    return render_template("blog.html", is_authenticated=current_user.is_authenticated)

@app.route("/reservation")
def reservation():
    return render_template("reservation.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        pass
        #hash password
    
    return render_template("login.html")


if __name__ == "__main__":
    app.run(host="127.0.0.1")