import boto3
import os
from dotenv import load_dotenv

load_dotenv()

file_name = 'test.txt'
bucket_name = 'meli-hosted-content'

s3_client = boto3.client(
        's3',
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
)

response = s3_client.upload_file(file_name, bucket_name, file_name)