from flask import Flask, jsonify, request, send_from_directory

# local
import classifier
from utils import STATIC_DIR, JS_DIR, VIEWS_DIR

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
    return send_from_directory(JS_DIR, path)

@app.route("/views/<path:path>")
def view(path):
    return send_from_directory(VIEWS_DIR, path)

@app.route("/")
def index():
    return send_from_directory(STATIC_DIR, "index.html")

if __name__ == "__main__":
    utils.config_logging()
    
    app.run(host='0.0.0.0', debug=True, port=3000)
