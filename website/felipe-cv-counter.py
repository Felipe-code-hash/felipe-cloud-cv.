import json
import os
import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(os.environ["TABLE_NAME"])


def lambda_handler(event, context):
    try:
        response = table.update_item(
            Key={"id": "home"},
            UpdateExpression="SET #count = if_not_exists(#count, :zero) + :one",
            ExpressionAttributeNames={
                "#count": "count"
            },
            ExpressionAttributeValues={
                ":zero": 0,
                ":one": 1
            },
            ReturnValues="UPDATED_NEW"
        )

        count = int(response["Attributes"]["count"])

        print(f"Contador actualizado correctamente: {count}")

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps({
                "count": count
            })
        }

    except ClientError as error:
        print(f"Error de DynamoDB: {error}")

        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps({
                "error": "No se pudo actualizar el contador"
            })
        }

    except Exception as error:
        print(f"Error inesperado: {error}")

        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps({
                "error": "Error interno del servidor"
            })
        }
