resource "aws_subnet" "main" {
  vpc_id     = "data.aws_vpc.id"
  cidr_block = "10.0.1.0/24"

  tags = {
    Name = "Main"
  }
}


resource "aws_route_table" "example" {
  vpc_id = "data.aws_vpc.id"

  route {
    cidr_block = "10.0.1.0/24"
    gateway_id = data.aws_nat_gateway.id
  }

  tags = {
    Name = "Main"
  }
}

resource "aws_iam_role_policy_attachment" "iam_role_policy_attachment_lambda_vpc_access_execution" {
  role       = data.DevOps-Candidate-Lambda-Role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaVPCAccessExecutionRole"
}

resource "aws_default_security_group" "default_security_group" {
  vpc_id = data.vpc-0de2bfe0f5fc540e0.id

  ingress {
    protocol  = -1
    self      = true
    from_port = 0
    to_port   = 0
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]

  }

}