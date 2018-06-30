from .IFileStorageMode import IFileStorageMode
from .File import File
import os


class FileSystem(IFileStorageMode):
    def __init__(self, location):
        self.location = os.path.abspath(location)

    def save_document(self, file_name, content):
        try:
            File(self.location).save_file(file_name, content)
        except:
            raise

    def open_document(self, file_name, mode):
        try:
            return File(self.location).open_file(file_name, mode)
        except:
            raise

    def get_size(self, file_name):
        return File(self.location).get_size(file_name)

    def get_creation_time(self, file_name):
        return File(self.location).get_creation_time(file_name)

    def get_updated_time(self, file_name):
        return File(self.location).get_updated_time(file_name)

    def rename_document(self, old_file_name, new_file_name):
        try:
            old_file = self.open_document(old_file_name)
            old_data = old_file.read()
            self.delete_document(old_file_name)
            self.save_document(new_file_name, old_data)
        except:
            raise

    def delete_document(self, file_name):
        try:
            File(self.location).delete_file(file_name)
        except:
            raise
