import json
import boto3


def lambda_handler(event, context):
    # remove this comment

    client = boto3.client("dynamodb")
    client.delete_item(TableName="websocket_ids",
                       Key={"connectionId": {"S": event["requestContext"].get("connectionId")}})

    return {
        'statusCode': 200,
        'body': json.dumps('A client has disconnected')
    }
