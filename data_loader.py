import gzip
import os
import csv
import random
import sys

reload(sys)  
sys.setdefaultencoding('utf-8')

# data folder
DATADIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'amazon')
REVIEW_DATA = os.path.join(DATADIR, 'Electronics.txt.gz')
TRAIN_FILE = os.path.join(DATADIR, 'train.csv')
TEST_FILE = os.path.join(DATADIR, 'test.csv')

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
        rest = l[colonPos+2:]
        entry[eName] = rest
    yield entry

def load_data(dev=True):
    rows = []
    for e in parse(REVIEW_DATA):
        try:
            row = ( int(float(e['review/score'])), e['review/summary'], e['review/text'] )
            rows.append(row)
        except KeyError:
            continue

    if dev:
        N = len(rows)
        test_N = 10000
        train = rows[:-test_N]
        test = rows[-test_N:]
    else:
        train = rows
        test = []

    print "train: %d" % len(train)
    with open(TRAIN_FILE, 'w') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerows(train)

    if dev:
        print "test: %d" % len(test)
        with open(TEST_FILE, 'w') as f:
            csvwriter = csv.writer(f)
            csvwriter.writerows(test)

if __name__ == '__main__':
    load_data(dev=True)