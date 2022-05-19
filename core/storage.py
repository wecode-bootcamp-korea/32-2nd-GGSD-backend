import boto3
import uuid

class MyS3Client:
    def __init__(self, access_key, secret_key, bucket_name):
        boto3_s3 = boto3.client(
            's3',
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key
        )
        self.s3_client = boto3_s3
        self.bucket_name = bucket_name

    def upload(self, file):
        try:
            file_id = str(uuid.uuid4())
            extra_args = {'ContentType': file.content_type}

            self.s3_client.upload_fileobj(
                file,
                self.bucket_name,
                file_id,
                ExtraArgs=extra_args
            )
            uploaded_url = f'https://{self.bucket_name}.s3.ap-northeast-2.amazonaws.com/{file_id}'
            return uploaded_url
        except:
            return None