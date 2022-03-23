from wsgiref.validate import validator
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from wtforms import Form, FileField, StringField, validators
from flask_login import LoginManager, UserMixin, login_user, current_user, logout_user
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "uuuuuuu_secret_keeeyyyy"
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
    try:    
        return User.query.get(user_id)
    except:
        return None

class EventForm(Form):
    name = StringField("Nombre", [validators.DataRequired()])
    description = StringField("Descripción", [validators.DataRequired()])
    date = StringField("Fecha", [validators.DataRequired()])
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
    print(current_user)
    return render_template("blog.html", current_user = current_user)

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
    error = ''
    if request.method == "POST":
        password = request.form["password"]
        # hashed_pass = bcrypt.generate_password_hash(password)
        hotel = User.query.first()
        hotel_pass = hotel.password
        is_password = bcrypt.check_password_hash(hotel_pass, password)
        
        if is_password:
            login_user(hotel)
            return redirect("/blog")
        else:
            error="Contraseña Incorrecta"

    
    return render_template("login.html", error = error)

@app.route("/logout")
def logout():
    logout_user()
    return redirect("/blog")


if __name__ == "__main__":
    app.run(host="127.0.0.1")