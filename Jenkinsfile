pipeline{
    agent any
    stages{
        stage("TF Init"){
            steps{
                echo "Executing Terraform Init"
                sh 'sudo yum install -y yum-utils'
                sh 'sudo yum-config-manager --add-repo https://rpm.releases.hashicorp.com/RHEL/hashicorp.repo'
                sh 'sudo yum -y install terraform'
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
                'terraform plan'
            }
        }
        stage("TF Apply"){
            steps{
                echo "Executing Terraform Apply"
                sh 'terraform apply --auto-approve'
            }
        }
        stage("Invoke Lambda"){
            steps{
                echo "Invoking your AWS Lambda"
                aws lambda invoke --function-name lambda-security_group-tf-lambda-function out.txt
                 {
    "StatusCode": 200,
    "LogResult": "U1RBUlQgUmVxdWVzdElkOiAyMjVjNTNmZC1hYTg0LTQwMzgtODA0OS1iYTYwN2M5ZmZjMWQgVmVyc2lvbjogJExBVEVTVAp7Im1lc3NhZ2UiOiAiTWVzc2FnZSBwcm9jZXNzZWQgc3VjY2Vzc2Z1bGx5LiJ9CjIwMApFTkQgUmVxdWVzdElkOiAyMjVjNTNmZC1hYTg0LTQwMzgtODA0OS1iYTYwN2M5ZmZjMWQKUkVQT1JUIFJlcXVlc3RJZDogMjI1YzUzZmQtYWE4NC00MDM4LTgwNDktYmE2MDdjOWZmYzFkCUR1cmF0aW9uOiAyODY1LjA2IG1zCUJpbGxlZCBEdXJhdGlvbjogMjg2NiBtcwlNZW1vcnkgU2l6ZTogMTI4IE1CCU1heCBNZW1vcnkgVXNlZDogNDkgTUIJSW5pdCBEdXJhdGlvbjogMzQzLjUxIG1zCQo=",
    "ExecutedVersion": "$LATEST"
}
                
            }
        }
    }
}
