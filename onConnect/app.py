import json
import boto3

def lambda_handler(event, context):
    # to check if deploy works
    print(event)
    client = boto3.client("dynamodb")
    client.put_item(
        TableName="websocket_ids",
        Item={
            "connectionId": {"S": event["requestContext"].get("connectionId")},
            "shopId": {"S": event['queryStringParameters']['shopId']},
            "connectionType": {"S": event['queryStringParameters']['connectionType']}
        }
        )
    return {
        'statusCode': 200,
        'body': json.dumps('A client has connected!')
    }
