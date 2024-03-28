import json
import boto3
from boto3.dynamodb.conditions import Key

dynamodb_resource = boto3.resource("dynamodb")
table = dynamodb_resource.Table("lotion-30143555")


def lambda_handler(event, context):
   email = event["queryStringParameters"]["email"]

   try:
       response = table.query(
           KeyConditionsExpression = Key("email").eq(email)
       )


       items = response["Items"]
       if(len(items) == 0):
               return []
       else:
            return items
  
      
   except Exception as exp:
       return {
           "statusCode": 401,
           "body": json.dumps({
               "message": str(exp)
           })
       }

