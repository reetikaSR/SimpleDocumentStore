from abc import abstractmethod


class IFileStorageMode:
    @abstractmethod
    def save_document(self, file_name, content, bucket_name=''):
        pass

    @abstractmethod
    def open_document(self, file_name, mode, bucket_name=''):
        pass

    @abstractmethod
    def get_size(self, file_name, bucket_name=''):
        pass

    @abstractmethod
    def get_creation_time(self, file_name, bucket_name=''):
        pass

    @abstractmethod
    def get_updated_time(self, file_name, bucket_name=''):
        pass

    @abstractmethod
    def rename_document(self, old_file_name, new_file_name, bucket_name=''):
        pass

    @abstractmethod
    def delete_document(self, file_name, bucket_name=''):
        pass
