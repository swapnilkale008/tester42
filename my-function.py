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




   

pipeline {
    agent any
    
    stages {
        stage('Invoke Lambda') {
            steps {
                sh '''
                    #!/usr/bin/env python3
                    
                    import requests

                    # Define the API endpoint URL
                    url = "https://2xfhzfbt31.execute-api.eu-west-1.amazonaws.com/candidate-email_serverless_lambda_stage/data"

                    # Define the payload data
                    payload = {
                        "subnet_id": "<Your Private Subnet ID>",
                        "name": "<Your Full Name>",
                        "email": "<Your Email Address>"
                    }

                    # Define the security headers
                    headers = {
                        "X-Siemens-Auth": "test"
                    }

                    # Make the HTTP request
                    response = requests.post(url, json=payload, headers=headers)

                    # Print the response status code and content
                    print(f"Response status code: {response.status_code}")
                    print(f"Response content: {response.content}")
                '''
            }
        }
    }
}
