# Movie API

Serverless API utilizing AWS to store data about movies using Python (3.7) Serverless Framework.

Serverless.yml handles the routing of the lambdas to their mapping to the API Gateway
Database connections are handled through the PynamoDB connector

The mocks folder contains useful payloads for testing

## Requirements
Python 3.7
Serverless Framework
NodeJS
AWSCLI

## Run the project
To get this running on your local machine clone this repo, set up your access_key and secret_access_key in ~/.aws/config and then run 
```
npm install 
sls install plugin serverless-python-requirements
terraform apply infra
serverless deploy
```

The infrastructure you need will be spun up with Terraform and Serverless make a note of the endpoints given back after the serverless deploy command has finished

The endpoints are protected via a Cognito authorizer so you'll need to create a cognito user with the following commands

```
aws cognito-idp sign-up \
    --region us-east-1 \
    --client-id 7qbu7uu8cp8soqudno2578je4p \
    --username example \
    --password Passw0rd!

aws cognito-idp admin-confirm-sign-up \
    --region us-east-1 \
    --user-pool-id us-east-1_la6Bl4dEZ \
    --username example
```

Once the user is created you'll need to get back your IdToken to pass to any curl commands

```
aws cognito-idp initiate-auth --auth-flow USER_PASSWORD_AUTH --client-id 7qbu7uu8cp8soqudno2578je4p --region us-east-1 --auth-parameters "{\"USERNAME\": \"example\", \"PASSWORD\": \"Passw0rd\!\"}"
```

This will give back an AccessToken, a RefreshToken, and an IdToken, copy the IdToken and append it to the header of any curl calls you want to make against the API

```
curl -H "Authorization:EXAMPLE-TOKEN" https://example-aws-endpoint/movies/
```
