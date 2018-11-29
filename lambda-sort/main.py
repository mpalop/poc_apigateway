#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from sorter import *
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
    logger.info("Entering in sort method")
    logger.info("Received event: " + str(event) + " type:" + str(type(event)))

    text = event["text"]
    sortoption = event["sortoption"]

    persist = Persistor()
    result = text_sort(text, sortoption)
    if result:
        code, status = persist.persist(original=text, filename="Sorted.json",payload=result)
        return response_proxy(code, result, 200)
    else:
        return response_proxy("Bad sortoption",
                              "Error using {} as sortoption".format(sortoption),
                              "sort",
                              503)