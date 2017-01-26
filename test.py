import os

import fasttext as ft

# local
from utils import STATIC_DIR, JS_DIR, VIEWS_DIR, RESULT_DIR, MODEL_NAME

# logging
import utils
import logging

logger = logging.getLogger("fasttext")

# load model
model_file = os.path.join(RESULT_DIR, MODEL_NAME)
classifier = ft.load_model(model_file + '.bin', label_prefix= '__label__')

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

    result = {'status': 0, 'prediction': labels}

     return result

content = {'title': '', 'text': 'this is excellent'}
make_prediction(content)
