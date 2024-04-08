from flask import Flask, render_template, send_from_directory, request, make_response

app = Flask(__name__)



@app.route("/",methods=["GET"])
def index():

    return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0',port="6000")