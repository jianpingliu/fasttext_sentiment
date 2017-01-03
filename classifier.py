import os
import re
import subprocess
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

# logging
import utils
import logging

logger = logging.getLogger("fasttext")

# data folder
from utils import DIR, DATA_DIR, RESULT_DIR

# data file
DATA_FILE = 'text'
MODEL_NAME = 'amazon.bin'

def predict(content):
    logger.info("title: %s", content['title'])
    logger.info("text: %s", content['text'])

    status1 = write_file(content)
    status2, prediction = call_fasttext()

    status = status1 or status2

    logger.info("status: %d", status)
    logger.info("prediction: %s", prediction)

    if status == 1:
        prediction = []
    result = {'status': status, 'prediction': prediction}
    return result

def write_file(content):
    title = content['title']
    text = content['text'][:2000]

    if title == '' and text == '':
        status = 1
    else:
        status = 0

    text = '1,%s,%s' % (title, text)

    # clean text
    text = utils.normalize_text(text)

    with open(os.path.join(DATA_DIR, DATA_FILE), 'w') as f:
        f.write(text)

    return status

def call_fasttext():
    if not os.path.exists(os.path.join(DIR, 'fasttext')):
        logger.error("fasttext does not exist")
        return 1

    if not os.path.exists(os.path.join(DATA_DIR, DATA_FILE)):
        logger.error("data/native_content does not exist")
        return 2

    try:
        cmd = "{0}/fasttext predict-prob {1}/{2} {3}/{4} 5"
        cmd = cmd.format(DIR, RESULT_DIR, MODEL_NAME, DATA_DIR, DATA_FILE)
        prediction = subprocess.check_output(cmd, shell=True)

        prediction = prediction.replace('\n', '').replace('__label__', '').split(' ')
        labels = map(int, prediction[0::2])
        scores = map(float, prediction[1::2])
        result = map(lambda (k, v): {'rating': k, 'score': v}, zip(labels, scores))
        status = 0
    except:
        logger.error("call fasttext failed")
        status, result = 3, []

    return status, result