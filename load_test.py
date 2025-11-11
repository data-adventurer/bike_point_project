from dotenv import load_dotenv
import boto3
import os

load_dotenv()

aws_access_key = os.getenv('aws_access_key')
aws_secret_key = os.getenv('aws_secret_access_key')
bucket = os.getenv('aws_bucket')

s3_client = boto3.client(
    's3'
    ,aws_access_key_id = aws_access_key
    ,aws_secret_access_key = aws_secret_key 
)

filename = 'data/2025-11-10T11-41.json'
s3filename = '2025-11-10T11-41.json'

s3_client.upload_file(filename, bucket, s3filename)