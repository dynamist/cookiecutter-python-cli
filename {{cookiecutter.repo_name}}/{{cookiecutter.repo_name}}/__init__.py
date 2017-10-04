# -*- coding: utf-8 -*-

""" {{cookiecutter.repo_name}} """

# python std lib
import os
import logging
import logging.config
import random
import string
import tempfile

__author__ = '{{cookiecutter.full_name}}'
__email__ = '{{cookiecutter.email}}'
__version__ = '{{cookiecutter.version}}'
__url__ = '{{cookiecutter.url}}'
__devel__ = True

PACKAGE_NAME = "{{cookiecutter.repo_name}}"

log_level_to_string_map = {
    5: "DEBUG",
    4: "INFO",
    3: "WARNING",
    2: "ERROR",
    1: "CRITICAL",
    0: "INFO"
}

random_log_file = os.path.join(
    tempfile.gettempdir(),
    '{{cookiecutter.repo_name}}-' +
    ''.join(random.SystemRandom().choice(string.ascii_lowercase)
            for _ in range(12)) + '.log',
)


def init_logging(log_level):
    """
    Init logging settings with default set to INFO.

    """
    level = log_level_to_string_map[log_level]

    if level in os.environ:
        msg = "%(levelname)s - %(name)s:%(lineno)s - %(message)s"
    else:
        msg = "%(levelname)s - %(message)s"

    logging_conf = {
        "version": 1,
        "root": {
            "level": level,
            "handlers": [],
        },
        "loggers": {
            "{{cookiecutter.repo_name}}": {
                "level": "DEBUG",
                "handlers": ["file", "console"],
            }
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "level": level,
                "formatter": "simple",
                "stream": "ext://sys.stdout"
            },
            "file": {
                "class": "logging.FileHandler",
                "level": "DEBUG",
                "formatter": "simple",
                "filename": random_log_file,
            }
        },
        "formatters": {
            "simple": {
                "format": " {}".format(msg)
            }
        }
    }

    logging.config.dictConfig(logging_conf)
