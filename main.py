# from crypt import methods
import base64
from werkzeug.datastructures import FileStorage
from io import BytesIO
from wsgiref.validate import validator
from flask import Flask, render_template, request, redirect, send_file, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import FileField, StringField, validators, DateField, SubmitField
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
    img_file = db.Column(db.LargeBinary)
    img_name = db.Column(db.String()) 
    name = db.Column(db.String(), nullable=False)
    description = db.Column(db.String(), nullable=False)
    date = db.Column(db.String(), nullable=False)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(), nullable=False)

db.create_all()

@login_manager.user_loader
def load_user(user_id):
    try:    
        return User.query.get(user_id)
    except:
        return None

class EventForm(FlaskForm):
    name = StringField("Nombre", validators=[validators.DataRequired()])
    description = StringField("Descripción", validators=[validators.DataRequired()])
    date = StringField("Fecha", validators=[validators.DataRequired()])
    image = FileField("Imagen", validators=[validators.DataRequired()])
    submit = SubmitField("Añadir")

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
    events = Event.query.all()
    return render_template("blog.html", current_user = current_user, events = events, BytesIO=BytesIO, b64 = base64)

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

@app.route("/addevent", methods=["GET", "POST"])
def addevent():
    form = EventForm()

    if request.method == "POST":
        img = form.image.data
        img_nm = img.filename
        img64 = img.read()
        new_event = Event(
            img_file = img64,
            img_name = img_nm,
            name = form.name.data,
            description = form.description.data,
            date = form.date.data
        )
        print(img_nm)
        # print(form.image.data)
        # print(form.name.data)
        # print(form.description.data)
        # print(form.date.data)
        db.session.add(new_event)
        db.session.commit()

        return redirect("/blog")

    return render_template("addevent.html", form=form)

@app.route("/edit:<id>", methods=["GET", "POST"])
def edit_event(id):
    event = Event.query.get(id)
    print(event)
    print("hello")
    form = EventForm()
    form.name.data = event.name
    form.description.data = event.description
    form.date.data = event.date
    form.image.process_data(base64.b64encode(event.img_file).decode("utf-8"))
    #  FileStorage(stream=event.img_file, filename = event.img_name) 
    # base64.b64encode(event.img_file).decode("utf-8")

    print(request.method)

    if request.method == "POST":
        form = EventForm()
        # img = form.image.data
        # print(img)
        # img_name = img.filename
        # img_file = img.read()
        
        # event.img_name = img_name
        edited_event = Event(
            id = event.id,
            img_file = form.image.data.read(),
            name = form.name.data,
            description = form.description.data,
            date = form.date.data
        )

        print(edited_event)  

        db.session.delete(event)
        db.session.add(edited_event)
        db.session.commit()

        return redirect(url_for("blog"))

    return render_template("edit_event.html", form = form, id=event.id)

@app.route("/changepwd", methods=["GET", "POST"])
def change_password():
    error = None
    if request.method == "POST":
        pwd = User.query.first()
        old_pass = request.form["oldEmail"]
        new_pass = request.form["newEmail"]
        new_hash_pass = bcrypt.generate_password_hash(new_pass)

        print(pwd)
        print(old_pass)
        print(new_pass)

        is_pass = bcrypt.check_password_hash(pwd.password, old_pass)

        if is_pass: 
            new_pwd = User(id = pwd.id, password = new_hash_pass)

            db.session.delete(pwd)
            db.session.add(new_pwd)
            db.session.commit()

            return redirect("/blog")
        elif not is_pass:
            error = "Contraseña Incorrecta"
        else:
            error = "Something went wrong"

    return render_template("changepwd.html", error = error)

@app.route("/delete:<id>")
def delete(id):
    item_to_delete = Event.query.get(id)
    db.session.delete(item_to_delete)
    db.session.commit()
    return redirect("/blog")



if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True)