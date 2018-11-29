#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import re

logger = logging.getLogger()
logger.setLevel(logging.INFO)

SORTOPTIONS=("NOSORT","ASCENDING","DESCENDING")


def text_sort(text, sortoption):
    if sortoption not in SORTOPTIONS:
        logger.error("sortoption must be: {}".format(",".join(SORTOPTIONS)))
        return ""

    parser = re.compile("(\w+)", re.IGNORECASE | re.MULTILINE)
    if sortoption == "NOSORT":
        words = parser.findall(text)
        logger.info("text of {} words has been processed".format(len(words)))
    if sortoption == "ASCENDING":
        words = sorted(parser.findall(text), key=lambda x:x.lower())
        logger.info("text of {} words has been processed and sorted {}".format(len(words), sortoption.lower()))
    if sortoption == "DESCENDING":
        words = sorted(parser.findall(text), key=lambda x:x.lower(), reverse=True)
        logger.info("text of {} words has been processed and sorted {}".format(len(words), sortoption.lower()))
    return words