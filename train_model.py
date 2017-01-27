import os
import fasttext as ft

# path
from utils import DATA_DIR, DIR, RESULT_DIR, MODEL_NAME

# logging
import utils
import logging

logger = logging.getLogger("fasttext")

TRAIN_FILE = os.path.join(DATA_DIR, 'train.data')
TEST_FILE = os.path.join(DATA_DIR, 'test.data')


def main():
    input_file = TRAIN_FILE
    out_file = os.path.join(RESULT_DIR, MODEL_NAME)
    classifier = ft.supervised(
        input_file,
        out_file,
        dim=20,
        lr=0.25,
        word_ngrams=2,
        min_count=20,
        bucket=1000000,
        epoch=5,
        thread=10,
        silent=0,
        label_prefix="__label__")

    # test the classifier
    result = classifier.test(TEST_FILE)

    logger.info('P@1: %s', result.precision)
    logger.info('R@1: %s', result.recall)
    logger.info('Number of examples: %s', result.nexamples)


if __name__ == '__main__':
    utils.config_logging()
    main()
