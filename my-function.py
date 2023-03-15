import requests

def lambda_handler(event, context):
    payload = {
        "subnet_id": "10.0.1.0/24",
        "name": "swapnil kale",
        "email": "swapnilkale2504@gmail.com"
    }
    headers = {
        "X-Siemens-Auth": "test"
    }
    url = "https://2xfhzfbt31.execute-api.eu-west-1.amazonaws.com/candidate-email_serverless_lambda_stage/data"
    response = requests.post(url, headers=headers, json=payload)
    print(response.status_code)
    print(response.text)


   

