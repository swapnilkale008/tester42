
resource "aws_subnet" "private" {
  vpc_id            = data.aws_vpc.id
  cidr_block        = "10.0.1.0/24"
}

resource "aws_route_table" "private" {
  vpc_id = data.aws_vpc.vpc.id
}

resource "aws_route" "private_nat_gateway" {
  route_table_id         = aws_route_table.private.id
  destination_cidr_block = "0.0.0.0/0"
  nat_gateway_id         = data.aws_nat_gateway.nat.id
}

resource "aws_route_table_association" "private" {
  subnet_id      = aws_subnet.private.id
  route_table_id = aws_route_table.private.id
}

# create the Lambda function
resource "aws_lambda_function" "test" {
  filename         = "test.zip"
  function_name    = "test_function"
  role             = data.aws_iam_role.lambda.arn
  handler          = "index.handler"
  runtime          = "nodejs12.x"
  source_code_hash = filebase64sha256("test.zip")
}

resource "aws_security_group" "test" {
  name_prefix = "security_group"
  vpc_id      = data.aws_vpc.vpc.id

  ingress {
    from_port = 0
    to_port   = 65535
    protocol  = "tcp"
    cidr_blocks = [
      "10.0.0.0/16"
    ]
  }

  egress {
    from_port = 0
    to_port   = 65535
    protocol  = "tcp"
    cidr_blocks = [
      "0.0.0.0/0"
    ]
  }
}

data "aws_iam_policy_document" "lambda_policy" {
  statement {
    effect = "Allow"
    actions = [
      "logs:CreateLogGroup",
      "logs:CreateLogStream",
      "logs:PutLogEvents"
    ]
    resources = ["arn:aws:logs:*:*:*"]
  }
}

data "aws_iam_role" "lambda_role" {
  name = data.aws_iam_role.lambda.arn
}
