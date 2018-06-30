SimpleDocumentStore is used to store the documents on the local file system or AWS S3.
This can be easily configured by sending the storage mode during the creation of the storage mode.
Default storage mode is 'local'.
For S3, send 'aws' as storage mode.
It is written in python3.6


Installation:
pip3 install SimpleDocumentStore

Usage:
import SimpleDocumentStore

AWS:
storage_mode = SimpleDocumentStore.create_storage_mode(local_path,
                                                   'aws',
                                                  aws_access_key,
                                                  aws_secret_key
                                                  )
send the bucket name for S3.

Local:
storage_mode = SimpleDocumentStore.create_storage_mode(local_path)

Operations:
storage_mode.save_document(self, file_name, content, bucket_name)
storage_mode.open_document(self, file_name, mode, bucket_name)
storage_mode.get_size(self, file_name, bucket_name)
storage_mode.get_creation_time(self, file_name, bucket_name)
storage_mode.get_updated_time(self, file_name, bucket_name)
storage_mode.rename_document(self, old_file_name, new_file_name, bucket_name)
storage_mode.delete_document(self, file_name, bucket_name)

