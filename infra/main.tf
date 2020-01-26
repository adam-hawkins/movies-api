provider "aws" {
  region = "us-east-1"
}

#create the dynamo table
resource "aws_dynamodb_table" "movies" {
  name           = "movies"
  billing_mode   = "PROVISIONED"
  read_capacity  = 1
  write_capacity = 1
  hash_key       = "id"

  attribute {
    name = "id"
    type = "S"
  }
}

# load in IAM template
data "template_file" "cognito_iam_assume_role_policy" {
  template = file("./movies-identity.json")

  vars = {
    cognito_identity_pool_id = aws_cognito_identity_pool.movies_identity_pool.id
  }
}

# create the IAM policy for cognito to use
resource "aws_iam_role" "authenticated" {
  name = "movies-identity"

  assume_role_policy = data.template_file.cognito_iam_assume_role_policy.rendered 
}

#create the cognito user pool
resource "aws_cognito_user_pool" "movies_user_pool" {
  name = "movies-user-pool"

  alias_attributes = [
    "email",
    "preferred_username",
  ]

  admin_create_user_config {
    allow_admin_create_user_only = false
  }

  password_policy {
    minimum_length    = 8
    require_uppercase = true
    require_lowercase = true
    require_numbers   = true
    require_symbols   = true
  }

  schema {
    name                = "email"
    attribute_data_type = "String"
    mutable             = false
    required            = false
  }
}

# generate client for the user pool
resource "aws_cognito_user_pool_client" "movies_user_pool_client" {
  name = "movies-user-pool-client"

  user_pool_id    = aws_cognito_user_pool.movies_user_pool.id
  generate_secret = false

  explicit_auth_flows = [
    "ADMIN_NO_SRP_AUTH",
    "USER_PASSWORD_AUTH",
  ]
}

# create the identity pool to actually federate users
resource "aws_cognito_identity_pool" "movies_identity_pool" {
  identity_pool_name = "movies identity pool"

  allow_unauthenticated_identities = false

  cognito_identity_providers {
    client_id               = aws_cognito_user_pool_client.movies_user_pool_client.id
    server_side_token_check = true

    provider_name = "cognito-idp.us-east-1.amazonaws.com/${aws_cognito_user_pool.movies_user_pool.id}"
  }
}

# attach an IAM policy to allow interaction with Dynamo
resource "aws_cognito_identity_pool_roles_attachment" "movies_IAM_role" {
  identity_pool_id = aws_cognito_identity_pool.movies_identity_pool.id
  #assume_role_policy = data.template_file.cognito_iam_assume_role_policy.rendered
  roles = {
    "authenticated" = aws_iam_role.authenticated.arn
  }
}

