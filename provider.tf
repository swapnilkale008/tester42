provider "aws" {
  region  = "eu-west-1" # Don't change the region
}

backend "s3" {
    bucket = "3.devops.candidate.exam"
    key    = "swapnil.kale"
    region = "eu-west-1"
  }
}