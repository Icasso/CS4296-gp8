import json


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
        # TODO database stuff

    return response
