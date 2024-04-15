from flask import render_template, Blueprint, request, flash
from hashlib import sha256

bp = Blueprint("web", __name__)

@bp.route("/")
def home():
    return render_template("homepage.html")

@bp.route("/", methods=('POST', 'GET'))
def login():
    if request.method == 'POST':
        username = request.form.get('username', False)
        password = request.form.get('password', False)

        if username == "admin123" and sha256(password.encode('utf-8')).hexdigest() == "426848eb68bf6aa07212a4070863dbe30d92456cf011e238252ddfd86a247856":
            return "INTRO_TO_CTF{h@Vv_D14_Y0u_G3t_1n}"
    return render_template("homepage.html")

@bp.route("/passwords")
def dbpage():
    return render_template("totally_authetnic_db.html")

@bp.route("/flag")
def flag():
    return "nice try lmao"
