from entities.email_entity import Email
import boto3
from botocore.exceptions import ClientError
from dotenv import load_dotenv
import os
from botocore.config import Config


class SendEmailWithAWS:
    
    def __init__(self):
        load_dotenv()         
        self.aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
        self.aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
        self.sender = "arthurchagas01@gmail.com"
        self.aws_region = os.getenv("AWS_REGION","us-east-2")
        my_config = Config(region_name =  self.aws_region, signature_version = 'v4', retries = {'max_attempts': 10, 'mode': 'standard'})
        self.client = boto3.client('ses', config=my_config, aws_access_key_id=self.aws_access_key_id, aws_secret_access_key= self.aws_secret_access_key)

    
    async def sendWithAWS(self, email):
        try:
            response = self.client.send_email(Source=self.sender, Destination={'ToAddresses': [email.to_email]}, Message={'Subject': {'Data': email.subject,'Charset': 'UTF-8'}, 'Body': {'Text': {'Data': email.body,'Charset': 'UTF-8'}}})
            print(f"Email sent! Message ID: {response['MessageId']} and {response['ResponseMetadata']['HTTPStatusCode']}")
            return response['ResponseMetadata']['HTTPStatusCode']
        except ClientError as e:
            print(f"Failed to send email: {e.response['Error']['Message']}")
            raise Exception("Failed to send email via SES")
    
    
    