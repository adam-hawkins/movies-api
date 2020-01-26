aws cognito-idp sign-up \
  --region us-east-1 \
  --client-id 7qbu7uu8cp8soqudno2578je4p \
  --username example \
  --password Passw0rd!

aws cognito-idp admin-confirm-sign-up \
  --region us-east-1 \
  --user-pool-id us-east-1_la6Bl4dEZ \
  --username example
