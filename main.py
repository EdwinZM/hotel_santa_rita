from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float, nullable=False)
    name = db.Column(db.String, unique=True, nullable=False)
    commodities = db.Column(db.String, nullable=False)
    size = db.Column(db.Float, nullable=False)

db.create_all()

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
    return render_template("blog.html")

@app.route("/reservation")
def reservation():
    return render_template("reservation.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(host="127.0.0.1")