import json
import boto3


def lambda_handler(event, context):
    # to check if deploy works

    client = boto3.client("dynamodb")
    client.delete_item(TableName="websocket_ids",
                       Key={"connectionId": {"S": event["requestContext"].get("connectionId")}})

    return {
        'statusCode': 200,
        'body': json.dumps('A client has disconnected')
    }
