import json
import boto3
from uuid import uuid4
import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Orders')

def productInfo(productCount, productName):
    return f"Your Order on {productCount} {productName}(s) have been made and being processed to our database"


def lambda_handler(event, context):
    response = {
        "sessionState": {
            "dialogAction": {
                "type": "Close"
            },
            "intent": {
                "name": "OrderIntent",
                "state": "Fulfilled"
            }
        },
        "messages": [
            {
                "contentType": "PlainText",
                "content": "",
            }
        ],
    }

    if event["sessionState"]["intent"]["name"] == "OrderIntent":
        productCount = event['sessionState']['intent']['slots']['productCount']['value']['interpretedValue']
        productName = event['sessionState']['intent']['slots']['productName']['value']['interpretedValue']
        response['messages'][0]['content'] = productInfo(
            productCount, productName)
        table.put_item(
            Item={
                "OrderID": str(uuid4()),
                "ProductName": productName,
                "Quantity": productCount,
                "OrderDateTime": datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
            }
        )

    return response
