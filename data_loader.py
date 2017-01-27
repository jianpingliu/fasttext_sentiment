import gzip
import os
import csv
import random

import utils

# data folder
DATA_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'data')
TRAIN_DATA_DIR = os.path.join(DATA_DIR, 'amazon')
REVIEW_DATA = os.path.join(TRAIN_DATA_DIR, 'Electronics.txt.gz')
TRAIN_FILE = os.path.join(TRAIN_DATA_DIR, 'train.csv')
TEST_FILE = os.path.join(TRAIN_DATA_DIR, 'test.csv')


def parse(filename):
    f = gzip.open(filename, 'r')
    entry = {}
    for l in f:
        l = l.strip()
        colonPos = l.find(':')
        if colonPos == -1:
            yield entry
            entry = {}
            continue
        eName = l[:colonPos]
        rest = l[colonPos + 2:]
        entry[eName] = rest
    yield entry


def load_data(dev=True):
    rows = []
    for e in parse(REVIEW_DATA):
        try:
            row = (int(float(e['review/score'])), e['review/summary'],
                   e['review/text'])
            rows.append(row)
        except KeyError:
            continue

    N = len(rows)
    test_N = 10000
    train = rows[:-test_N]
    test = rows[-test_N:]

    print "test: %d" % len(test)
    with open(TEST_FILE, 'w') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerows(test)


def normalize_text(input_filename, output_filename):
    with open(input_filename, 'r') as in_file:
        with open(output_filename, 'w') as out_file:
            for line in in_file:
                out_file.write(utils.normalize_text(line) + "\n")


if __name__ == '__main__':
    load_data()
    normalize_text(TRAIN_FILE, os.path.join(DATA_DIR, 'train.data'))
    normalize_text(TEST_FILE, os.path.join(DATA_DIR, 'test.data'))
