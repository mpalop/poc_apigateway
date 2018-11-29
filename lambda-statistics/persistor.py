#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import logging
import json
from hashlib import md5

import redis
import boto3


logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Lambda environment
BUCKET=os.environ["BUCKET_NAME"]
REDIS_ENDPOINT=os.environ["REDIS_ENDPOINT"]
ENVIRONMENT=os.environ["ENVIRONMENT"]
REDIS_HASH="PERSISTED"

def md5_checksum(text):
    result = md5(text.encode())
    return result.hexdigest()

def save_file(path, content):
    s3 = boto3.client("s3")
    res = s3.put_object(
        Bucket=BUCKET,
        Key=path,
        Body=content
    )
    return res


class Persistor(object):
    def __init__(self):
        self.s3 = boto3.client("s3")
        self.rcon = redis.StrictRedis(host=REDIS_ENDPOINT, port=6379, db=0)

    def get_status(self, code):
        res = self.rcon.hget(REDIS_HASH, code)
        if res:
            return json.loads(res), True
        else:
            return {}, False

    def save_status(self, code, status):
        res = self.rcon.hset(REDIS_HASH, code, json.dumps(status))
        return res

    def persist(self, original, filename, payload):
        code = md5_checksum(original)
        status, exists = self.get_status(code)
        if not exists:
            res_s3_original = save_file("{}/Original.json".format(code), json.dumps(original))

        if not status.get(filename,""):
            status[filename]=True
            res_s3 = save_file("{}/{}".format(code,filename),
                               json.dumps(payload, ensure_ascii=False).encode('utf-8'))

        self.save_status(code, status)
        return code, status





