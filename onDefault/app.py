import json


def lambda_handler(event, context):
    # to check if deploy works
    return {
        'statusCode': 200,
        'body': json.dumps('Default route invoked')
    }


