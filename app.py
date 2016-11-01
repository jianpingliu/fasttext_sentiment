from flask import Flask, jsonify, request, send_from_directory

# local
import classifier

# logging
import utils
import logging

logger = logging.getLogger("fasttext")

app = Flask(__name__)

@app.route("/api/classify_text", methods=['POST'])
def classify_text():
    data = request.get_json()
    content = data['content']
    response = classifier.predict(content)
    return jsonify(response)

@app.route("/js/<path:path>")
def js(path):
    return send_from_directory("static/app/js", path)

@app.route("/views/<path:path>")
def view(path):
    return send_from_directory("static/app/views", path)

@app.route("/")
def index():
    return send_from_directory("static", "index.html")

if __name__ == "__main__":
    utils.config_logging()
    
    app.run(host='0.0.0.0', debug=True, port=5555)
