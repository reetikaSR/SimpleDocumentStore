from .IFileStorageMode import IFileStorageMode
from .File import File
import boto3
import botocore


class AWSS3(IFileStorageMode):
    def __init__(self, access_key, secret_access_key, local_aws_path):
        self.location = local_aws_path
        self.s3_client = boto3.client('s3',
                                      aws_access_key_id=access_key,
                                      aws_secret_access_key=secret_access_key)
        self.s3_resource = boto3.resource('s3',
                                          aws_access_key_id=access_key,
                                          aws_secret_access_key=secret_access_key)

    def save_document(self, file_name, content, bucket_name):
        try:
            self.__create_bucket(bucket_name)
            full_path = File(self.location).save_file(file_name, content)
            self.s3_client.upload_file(full_path, bucket_name, file_name)
        except:
            raise

    def open_document(self, file_name, mode, bucket_name):
        try:
            self.s3_resource.Bucket(bucket_name).download_file(file_name, file_name + 's3')
            return File(self.location).open_file(file_name + 's3', mode)
        except:
            raise

    def get_size(self, file_name, bucket_name):
        self.s3_resource.Bucket(bucket_name).download_file(file_name, file_name + 's3')
        return File(self.location).get_size(file_name + 's3')

    def get_creation_time(self, file_name, bucket_name):
        self.s3_resource.Bucket(bucket_name).download_file(file_name, file_name + 's3')
        return File(self.location).get_creation_time(file_name + 's3')

    def get_updated_time(self, file_name, bucket_name):
        self.s3_resource.Bucket(bucket_name).download_file(file_name, file_name + 's3')
        return File(self.location).get_updated_time(file_name + 's3')

    def rename_document(self, old_file_name, new_file_name, bucket_name):
        try:
            old_file = self.open_document(old_file_name, 'r', bucket_name)
            old_data = old_file.read()
            self.delete_document(old_file_name, bucket_name)
            self.save_document(new_file_name, old_data, bucket_name)
        except:
            raise

    def delete_document(self, file_name, bucket_name):
        try:
            self.s3_client.delete_object(Bucket=bucket_name, Key=file_name)
        except:
            raise

    def __create_bucket(self, bucket_name):
        response = self.s3_client.list_buckets()
        buckets = [bucket['Name'] for bucket in response['Buckets']]
        for bucket in buckets:
            if bucket == bucket_name:
                return
        self.s3_client.create_bucket(Bucket=bucket_name)

    def __download_file(self, bucket_name, file_name):
        try:
            self.s3_client.Bucket(bucket_name).download_file(self.location, file_name)
        except botocore.exceptions.ClientError as e:
            if e.response['Error']['Code'] == "404":
                print("The object does not exist.")
            else:
                raise