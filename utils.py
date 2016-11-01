import json
import os
import logging
import logging.config

def config_logging():
    directory = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(directory, "logging_config.json")) as f:
        logging_config = json.load(f)
    assert isinstance(logging_config, dict)
    logging.config.dictConfig(logging_config)