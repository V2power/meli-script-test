import boto3

s3 = boto3.client('s3')
s3.download_file('meli-hosted-content', 'links.txt', 'links.txt')