## Script Allows you to connect AWS EC2 instance and S3 locally.

import boto3
import os
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

def connect_to_s3():
    try:
        s3 = boto3.client('s3')
        return s3
    except (NoCredentialsError, PartialCredentialsError):
        print("Credentials not available.")
        return None

def upload_file_to_s3(file_name, bucket_name, object_name=None):
    if object_name is None:
        object_name = os.path.basename(file_name)

    s3 = connect_to_s3()
    if s3:
        try:
            s3.upload_file(file_name, bucket_name, object_name)
            print(f"File {file_name} uploaded successfully.")
        except Exception as e:
            print(f"Error uploading file: {e}")

def download_file_from_s3(bucket_name, object_name, file_name=None):
    if file_name is None:
        file_name = os.path.basename(object_name)

    s3 = connect_to_s3()
    if s3:
        try:
            s3.download_file(bucket_name, object_name, file_name)
            print(f"Downloaded successfully.")
        except Exception as e:
            print(f"Error downloading file: {e}")

if __name__ == "__main__":
    bucket_name = ''
    file_name = ''
    object_name = ''

    upload_file_to_s3(file_name, bucket_name, object_name)
    download_file_from_s3(bucket_name, object_name, file_name)