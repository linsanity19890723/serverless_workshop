# serverless_workshop


Agenda:
## 1. Set Role for Lambda
step:
	1. IAM>IAM POLICY>Create policy
	copy paste to IAM policy
 ```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ],
      "Resource": "arn:aws:logs:*:*:*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "ec2:Start*",
        "ec2:Stop*",
        "ec2:DescribeInstances"
      ],
      "Resource": "*"
    }
  ]
}
 ```



2. IAM ROLE>Create an IAM ROL>Attach the Policy to the Role

## 2. Config Lambda:
	1. Select Python3.7
	2. Select Existing Role
## 3. Config SNS:
  	1. Amazon SNS>Topics>Create topic
  	2. Subscriptions>Create subscription
  	3. Select Protocol to "Email"
  	4. Input the email to "Endpoint"
  	5. Check your email and click "Confirm" to agree the suscription
  
## 4. Config Cloudwatch Event trigger
	1. Cloudwatch Event>Create Rule>Input cron expression
	ie.``46 07 * * ? *``
	2. Select Lambda function
 
