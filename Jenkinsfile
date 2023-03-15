pipeline{
    agent any
    stages{
        stage("TF Init"){
            steps{
                echo "Executing Terraform Init"
                sh 'yum install -y yum-utils'
                sh 'yum-config-manager --add-repo https://rpm.releases.hashicorp.com/RHEL/hashicorp.repo'
                sh 'yum -y install terraform'
                sh 'terraform init'
            }
        }
        stage("TF Validate"){
            steps{
                echo "Validating Terraform Code"
                sh 'terraform validate'
            }
        }
        stage("TF Plan"){
            steps{
                echo "Executing Terraform Plan"
                sh 'terraform plan'
            }
        }
        stage("TF Apply"){
            steps{
                echo "Executing Terraform Apply"
                sh 'terraform apply -auto-approve'
            }
        }
        stage("Invoke Lambda"){
            steps{
               sh '''
                    #!/usr/bin/env python3
                    
                    import requests
                    # Define the API endpoint URL
                    url = "https://2xfhzfbt31.execute-api.eu-west-1.amazonaws.com/candidate-email_serverless_lambda_stage/data"
                    # Define the payload data
                    payload = {
                        "subnet_id": "10.0.1.0/24",
                        "name": "swapnil kale",
                        "email": "swapnilkale2504@gmail.com"
                    }
                 
                    headers = {
                        "X-Siemens-Auth": "test"
                    }
                 
                    response = requests.post(url, json=payload, headers=headers)
                  
                    print(f"Response status code: {response.status_code}")
                    print(f"Response content: {response.content}")
                '''
            }
        }
    }
}
