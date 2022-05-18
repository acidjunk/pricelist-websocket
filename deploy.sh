sam validate --profile acidjunk
sam build --profile acidjunk --debug
sam package --profile acidjunk --s3-bucket websocket-server-bucket --region eu-central-1 --output-template-file out.yml
sam deploy --profile acidjunk --template-file out.yml --stack-name websocket-server-stack --region eu-central-1 --no-fail-on-empty-changeset --capabilities CAPABILITY_IAM