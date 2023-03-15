import requests

def lambda_handler(event, context):
    # Payload data
    payload = {
        "subnet_id": "10.0.1.0/24",
        "name": "swapnil kale",
        "email": "swapnilkale2504@gmail.com"
    }
    # Security header
    headers = {
        "X-Siemens-Auth": "test"
    }
    # API endpoint
    url = "https://2xfhzfbt31.execute-api.eu-west-1.amazonaws.com/candidate-email_serverless_lambda_stage/data"
    # Post request
    response = requests.post(url, headers=headers, json=payload)
    # Print response
    print(response.status_code)
    print(response.text)
