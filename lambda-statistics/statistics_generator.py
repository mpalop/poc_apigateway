#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import re

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def statistics_generator(text):
    parser = re.compile("(\w+)", re.IGNORECASE | re.MULTILINE)
    text_statistics = {}
    text_statistics['words'] = len(parser.findall(text))
    text_statistics['hyphens'] = text.count("-")
    text_statistics['spaces'] = text.count(" ")
    logger.info("processed text with {0[words]} words, {0[hyphens]} hyphens and {0[spaces]} spaces".format(text_statistics))
    return text_statistics
