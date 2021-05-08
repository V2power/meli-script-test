import boto3
import os
from dotenv import load_dotenv

load_dotenv()

s3 = boto3.resource('s3')
s3.Bucket('meli-hosted-content').download_file('links.txt', 'links.txt')