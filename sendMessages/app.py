import json
import boto3

# connection URL (i.e. backend URL).
def lambda_handler(event, context):
    # remove this comment
    dynamo = boto3.client("dynamodb")
    URL = "https://1n1v00okbh.execute-api.eu-central-1.amazonaws.com/prod"
    client = boto3.client("apigatewaymanagementapi", endpoint_url=URL)
    payload_connection_type = event["connectionType"]
    payload_shop_id = event["shopId"]
    test_body = ""

    clients_connected = dynamo.scan(TableName="websocket_ids")
    for connection in clients_connected["Items"]:
        client_connection_type = str(connection["connectionType"]["S"])
        client_shop_id = str(connection["shopId"]["S"])

        if payload_connection_type == client_connection_type and payload_shop_id == client_shop_id:
            msg = f"invalidate_{client_connection_type}_cache"
            response = client.post_to_connection(ConnectionId=connection["connectionId"]["S"], Data=json.dumps(msg))
        else:
            print(f"skipping {payload_connection_type}:{client_connection_type}//{payload_shop_id}:{client_shop_id}")

    return {
        'statusCode': 200,
        'body': "OK"
    }
