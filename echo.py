import json


def main(event, context):
    print(event)
    print('data is :', json.loads(event['body']))
