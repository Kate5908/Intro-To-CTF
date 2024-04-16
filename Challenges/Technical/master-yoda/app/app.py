from flask import Flask, render_template, send_from_directory, request, make_response, jsonify
import lxml.etree as etree  

app = Flask(__name__)



@app.route("/",methods=["GET"])
def index():
 
    return render_template("index.html")

@app.route("/kyber",methods=["GET"])
def kyber():
    if (request.method == "POST"):
        return render_template("zoom.html")
    return render_template("zoom.html")
@app.route("/store",methods=["POST"])
def store():
    if request.method == "POST":
        if 'xml' not in request.files:
            return jsonify({'status': 'no', 'message': 'No file part'})
        file = request.files['xml']
        xml = file.read()
        
        parser = etree.XMLParser(resolve_entities=True)
        root = etree.fromstring(xml,parser)
        xml_str = etree.tostring(root, pretty_print=True, encoding="unicode")
        return jsonify({'status':'yes','data':xml_str})

if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0',port="5000")