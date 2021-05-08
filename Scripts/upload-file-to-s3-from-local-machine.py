import boto3

s3 = boto3.client('s3')
s3.upload_file('file.txt', 'meli-hosted-content', 'file.text')
# nome_do_arquivo_a_ser_upado, nome_do_bucket, nome_do_arquivo_dentro_do_bucket