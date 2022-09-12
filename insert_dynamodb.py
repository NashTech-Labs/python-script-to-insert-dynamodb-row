#!/usr/bin/python3

import boto3
import argparse
import datetime
import time
import string
import random
import json
import uuid
import requests

"""
Get assumed session
returns: boto3 session
"""
def get_assumed_session():
    sts = boto3.client("sts")
    response = sts.assume_role(RoleArn="<role_arn>",
                               RoleSessionName="<role_name>")
    return boto3.session.Session(aws_access_key_id=response["Credentials"]["AccessKeyId"],
                                 aws_secret_access_key=response["Credentials"]["SecretAccessKey"],
                                 aws_session_token=response["Credentials"]["SessionToken"], region_name="<region>")


"""
param param1: Parameter one
param param2: Parameter two
param param3: Parameter three
"""
def insert_dynamo_row(param1, param2, param3):
    session = get_assumed_session()
    dynamo = session.client("dynamodb")

    dynamo.put_item(
        TableName="<table_name>",
        Item = {
            "Column1": {
                "S": param1
            },
            "Column2": {
                "S": param2
            },
            "Column3": {
                "S": param3
            },
            "RequestTimestamp": {
                "S": datetime.datetime.utcnow().isoformat()
            },
        }
    )