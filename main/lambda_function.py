import json
import requests

WEB_HOOK_URL = "WEBHOOK"

def lambda_handler(event, context):
    item = event["event"]
    if item["subtype"] == "add":
        text = ":" + item["name"] + ":" + "     " + "`" + ":" + item["name"] + ":" + "`"
        post_message(text)
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }

def post_message(text):
    requests.post(WEB_HOOK_URL, data = json.dumps({
        'text': text
    }))
