from flask import Flask, render_template, send_from_directory, request, make_response, redirect, url_for
import requests 
from urllib.parse import urlparse

app = Flask(__name__)



@app.route("/",methods=["GET"])
def index():
 
    return render_template("index.html")

@app.route("/vulnerable",methods=["GET"])
def vulnerable():
 
    return render_template("rickroll.html")

@app.route("/testing",methods=["GET"])
@app.route("/comment",methods=["GET"])
@app.route("/banking",methods=["GET"])
@app.route("/ping",methods=["GET"])
@app.route("/flag",methods=["GET"])
@app.route("/development",methods=["GET"])
def troll_lmao():
    return render_template("rickroll.html")
@app.route("/robots.txt",methods=["GET"])
def robots():
    return send_from_directory("static","robots.txt")

@app.route("/entrance",methods=["GET"])
def entrance():
    return redirect(url_for("muzz",url=""))
@app.route("/rave",methods=["GET"])
def muzz():
    
    url_value = request.args.get('url','')
    if (url_value):
        parsed = urlparse(url_value)
        print(parsed.hostname)
        if (parsed.hostname != 'app2'):
            return render_template("muzz.html",status="error")
        print("HELLO")
        return requests.get(url_value).text
    return render_template("muzz.html",status="pass")
if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0',port="5000")