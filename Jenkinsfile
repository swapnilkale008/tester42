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
                sh 'aws lambda invoke --function-name example_lambda --log-type Tail output.txt'
                sh 'echo "LogResult: $(cat output.txt | jq -r ".LogResult")"'
                sh 'echo "Decoded LogResult: $(cat output.txt | jq -r ".LogResult" | base64 --decode)"'
                
            }
        }
    }
}
