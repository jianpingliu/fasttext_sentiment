import os
import subprocess

# path
from utils import DATA_DIR, DIR, RESULT_DIR

# logging
import utils
import logging

logger = logging.getLogger("fasttext")

RAW_DATA_FILE = os.path.join(DATA_DIR, 'amazon', 'train.csv')
TRAIN_DATA_FILE = os.path.join(DATA_DIR, 'train.data')

def normalize_text(input_filename, output_filename):
    with open(input_filename, 'r') as in_file:
        with open(output_filename, 'w') as out_file:
            for line in in_file:
                out_file.write(utils.normalize_text(line) + "\n")

    logger.info("training data is normalized sucessfully")

def train_model():
    cmd = '''
          {0}/fasttext supervised \
           -input {1}/train.data \
           -output {2}/amazon \
           -dim 20 \
           -lr 0.25 \
           -wordNgrams 2 \
           -minCount 20 \
           -bucket 1000000 \
           -epoch 5 \
           -thread 10 \
           > /dev/null
        '''
    cmd = cmd.format(DIR, DATA_DIR, RESULT_DIR)
    subprocess.call(cmd, shell=True)

    logger.info("training model successfully")

def main():
    # normalize training data
    #normalize_text(RAW_DATA_FILE, TRAIN_DATA_FILE)

    # train model
    train_model()

if __name__ == '__main__':
    utils.config_logging()
    main()