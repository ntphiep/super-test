import boto3

s3_client = boto3.client('s3')

response = s3_client.list_buckets()

print(response)
