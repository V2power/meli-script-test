import boto3

s3 = boto3.client('s3')

bucket_name = 'meli-hosted-content' # Bucket criado no S3
directory_name = 'fury/arquivos_utilitários' # Criação da primeira pasta
s3.put_object(Bucket=bucket_name, Key=(directory_name+'/'))
directory_name = 'fury/arquivos_a_serem_analisados' # Criação da segunda pasta
s3.put_object(Bucket=bucket_name, Key=(directory_name+'/'))
