import os
import subprocess
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

# logging
import logging

logger = logging.getLogger("fasttext")

# data folder
DIR = os.path.dirname(os.path.abspath(__file__))
DATADIR = os.path.join(DIR, 'data')
RESULTSDIR = os.path.join(DIR, 'result')

# data file
DATA_FILE = 'text'
PREDICT_SCRIPT = 'predict.sh'
PREDICT_FILE = 'predict'

def predict(content):
    logger.info("title: %s", content['title'])
    logger.info("text: %s", content['text'])

    status1 = write_file(content)
    status2 = call_fasttext()
    status3, prediction = read_prediction()
    status = status1 or status2 or status3

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
    with open(os.path.join(DATADIR, DATA_FILE), 'w') as f:
        f.write('1,%s,%s' % (title, text))
    return status

def call_fasttext():
    try:
        shell_script = os.path.join(DIR, PREDICT_SCRIPT)
        cmd = "sh %s" % shell_script
        exit = subprocess.call(cmd, shell=True)
        status = 0
    except:
        status = 2
    return status

def read_prediction():
    prediction = []
    with open(os.path.join(RESULTSDIR, PREDICT_FILE), 'r') as f:
        prediction = f.readlines()

    if len(prediction) == 0:
        status, result = 3, []

    try:
        prediction = prediction[0].replace('\n', '').replace('__label__', '').split(' ')
        labels = map(int, prediction[0::2])
        scores = map(float, prediction[1::2])
        result = map(lambda (k, v): {'rating': k, 'score': v}, zip(labels, scores))
        status = 0
    except:
        status, result = 3, []
    return status, result