import os
import boto3
from dotenv import load_dotenv

load_dotenv()

def test_s3():
    s3_client = boto3.client(
        "s3",
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY")
    )
    bucket = os.getenv("S3_BUCKET_NAME")
    try:
        s3_client.head_bucket(Bucket=bucket)
        print(f"Success! Bucket '{bucket}' is accessible.")
    except Exception as e:
        print(f"Error: {str(e)}")

test_s3()