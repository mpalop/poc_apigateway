#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from statistics_generator import *
from persistor import *

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def response_proxy(code, text, return_code):
    response = dict()
    response["isBase64Encoded"] = False
    response["statusCode"] = return_code
    response['headers'] = {
        "Content-Type": "application/json"
    }
    data = dict()
    data["Code"]=code
    data["Text"]=text
    response["body"]=data
    return response

def lambda_handler(event, context):
    logger.info("Entering in statistics method")
    logger.info("Received event: " + str(event) + " type:" + str(type(event)))

    text = event["text"]

    persist = Persistor()
    result = statistics_generator(text)
    code, status = persist.persist(original=text, filename="TextStatistics.json", payload=result)
    return response_proxy(code, result, 200)
