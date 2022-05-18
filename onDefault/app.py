import json


def lambda_handler(event, context):
    # remove this comment
    return {
        'statusCode': 200,
        'body': json.dumps('Default route invoked')
    }


