from flask import Flask, render_template, send_from_directory, request
import os

app = Flask(__name__)

@app.route("/",methods=["GET"])
def index(): 
    return render_template("index.html")

@app.route("/vuln",methods=["GET"])
def vulnerable():
    return render_template("vuln.html")


@app.route("/robots.txt",methods=["GET"])
def robots():
    return send_from_directory("static","robots.txt")

@app.route("/tools/search", methods=["POST"])
def search():
        term = request.form.get('q')
        result = os.popen('ls tools | grep ' + term)

        html = """<!DOCTYPE html>
        <header>
                <title>The Sandbox</title>
                <style>
                        body {
                                background-image: url('/static/vuln.png');
                                height: 100%;
                                background-repeat: no-repeat;
                                background-size: cover;
                        }
                        div {
                                margin: 0;
                                position: absolute;
                                top: 50%;
                                left: 50%;
                                transform: translate(-50%, -50%);
                        }
                </style> 
        </header>
        <body>
                <centre>
                <div>
                <form method="post" action="/tools/search">
                        <input type="search" id="query" name="q" placeholder="Search...">
                        <input type="submit" name="submit" value="tools"/>
                </form>
        """
        for i in result.readlines():
             html += "<p>" + i + "</p>"
        html += "</div></centre></body>"
        return html


if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0',port="4999")