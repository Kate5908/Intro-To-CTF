from flask import Flask, render_template, send_from_directory, request
from random import randint


app = Flask(__name__)

@app.route("/",methods=["GET"])
def index(): 
    return render_template("index.html")

@app.route("/image1", methods=["GET"])
def image1():
    img = randint(1, 6)

    return render_template("image1.html", status=str(img))

@app.route("/image2", methods=["GET"])
def image2():
    img = randint(1, 5)

    return render_template("image2.html", status=str(img))

@app.route("/image3", methods=["GET"])
def image3():
    img = randint(1, 6)

    return render_template("image3.html", status=str(img))

@app.route("/image4", methods=["GET"])
def image4():
    img = randint(1, 6)
    print(img)

    return render_template("image4.html", status=str(img))

if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0',port="4999")