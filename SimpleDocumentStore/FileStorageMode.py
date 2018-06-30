from .AWSS3 import AWSS3
from .FileSystem import FileSystem


def create_storage_mode(local_location, file_storage_mode='local', aws_access_key='', aws_secret_key=''):
    if file_storage_mode == 'local':
        return FileSystem(local_location)
    elif file_storage_mode == 'aws':
        return AWSS3(aws_access_key, aws_secret_key, local_location)
    raise Exception("The storage mode should be local or aws")
