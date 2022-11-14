from flask import Flask
from flask import render_template
from flask import request
import random
import os
from flask import url_for
from flask_sqlalchemy import SQLAlchemy
from flask import redirect

app = Flask(__name__)
#app.config["DEBUG"] = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Urls.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
@app.before_first_request
def create_tables():
    db.create_all()


class Urls(db.Model):
    id_ = db.Column("id_", db.Integer, primary_key = True)
    long = db.Column("long", db.String())
    short = db.Column("short", db.String(10))

    def __init__(self, long, short):
        self.long = long
        self.short = short


def shorten_url():
    letters = string.ascii_lowercase + string.ascii_uppercase
    rand_letters = random.choice(letters, k = 3)
    rand_letters = "".join(rand_letters)
    short_url = Urls.query.filtter_by(short=rand_letters).frist()
    if not short_url:
        return rand_letters


@app.route("/", methods = ["POST", "GET"])
def home():
    if request.method == "POST":
        url_received = request.form['nm']
        found_url = Urls.query.filtter_by(long = url_received).frist()

        if found_url:
            return redirect(url_for("display_short_url", found_url.short))
        else:
            short_url = shorten_url()
            print(short_url)
            new_url = Urls(url_received, short_url)
            db.session.add(new_url)
            db.session.commit()


            return redirect(url_for("display_short_url", url = short_url))

    else:
        return render_template("input_url.html")

@app.route("/<short_url>")
def redirection(short_url):
    long_url = Urls.query.filtter_by(short = short_url).frist()

    if long_url:
        return redirect(long_url.long)
        
    else:
        return f"<h1> Url doesent not exit </h1>"

@app.route("/display/<url>")
def display_short_url(url):
    return url

@app.route('/all_urls')
def display_all():
    return Urls.query.all()


if __name__ == "__main__":
    app.run(port = 5000, debug = True)
