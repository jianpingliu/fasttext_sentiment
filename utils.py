import json
import os
import logging
import logging.config

import re

# path
DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(DIR, "data")
RESULT_DIR = os.path.join(DIR, "result")
STATIC_DIR = os.path.join(DIR, "static")
APP_DIR = os.path.join(STATIC_DIR, "app")
JS_DIR = os.path.join(APP_DIR, "js")
VIEWS_DIR = os.path.join(APP_DIR, "views")

MODEL_NAME = "amazon"


def config_logging():
    directory = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(directory, "logging_config.json")) as f:
        logging_config = json.load(f)
    assert isinstance(logging_config, dict)
    logging.config.dictConfig(logging_config)


def normalize_text(s):
    s = s.lower()
    s = re.sub(r"[^a-z0-9\!\%\(\)\',\.\?]", " ", s)
    s = re.sub(r"^", "__label__", s)
    s = re.sub(r"'", " ' ", s)
    s = re.sub(r'"', '', s)
    s = re.sub(r"\.", " . ", s)
    s = re.sub(r",", " , ", s)
    s = re.sub(r"\(", " ( ", s)
    s = re.sub(r"\)", " ) ", s)
    s = re.sub(r"\!", " ! ", s)
    s = re.sub(r"\?", " ? ", s)
    s = re.sub(r"\%", " % ", s)
    s = re.sub(r"\s{2,}", " ", s)
    return s
