import os
from flask import Flask, jsonify, request, send_from_directory
import fasttext as ft

# local
from utils import STATIC_DIR, JS_DIR, VIEWS_DIR, RESULT_DIR, MODEL_NAME

# logging
import utils
import logging

logger = logging.getLogger("fasttext")

# load model
model_file = os.path.join(RESULT_DIR, MODEL_NAME)
classifier = ft.load_model(model_file + '.bin', label_prefix='__label__')


def make_prediction(content):
    logger.info("title: %s", content['title'])
    logger.info("text: %s", content['text'])

    title = content['title']
    text = content['text'][:2000]

    text = ',%s.%s' % (title, text)

    # clean text
    text = utils.normalize_text(text)

    labels = classifier.predict_proba([text], k=5)[0]

    labels = map(lambda (k, v): {'rating': k, 'score': v}, labels)

    logger.info("prediction: %s", labels)

    result = {'status': 0, 'prediction': labels}

    return result


app = Flask(__name__)


@app.route("/api/classify_text", methods=['POST'])
def classify_text():
    data = request.get_json()
    content = data['content']

    response = make_prediction(content)

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
