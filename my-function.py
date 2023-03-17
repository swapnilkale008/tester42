import json
import boto3
import requests

def lambda_handler(event, context):
    # Define the payload
    payload = {
        "subnet_id": "10.0.1.0/16",
        "name": "swapnil kale",
        "email": "swapnilkale008@gmail.com"
    }
    
    # Define the header
    headers = {'X-Siemens-Auth': 'test'}
    
    # Make the request
    response = requests.post('https://2xfhzfbt31.execute-api.eu-west-1.amazonaws.com/candidate-email_serverless_lambda_stage/data', data=json.dumps(payload), headers=headers)

    # Log the response status code
    print(response.status_code)

    return {
        'statusCode': response.status_code,
        'body': json.dumps('Hello from Lambda!')
    }
