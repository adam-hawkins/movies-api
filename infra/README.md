# Movie Infra
Infrastructure as code for the movie api. This would normally be its own repo, but given the scope of this project it's placed placed within the main repo

For this we currently need:
- DynamoDB table
- Cognito User Pool
- Cognito Identity Pool
- IAM Role for Federated Users
- API Gateway (handled by Serverless Framework)
- Lambda Functions (handled through the Python code and deployed by Serverless Framework)
