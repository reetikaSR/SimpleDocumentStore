import os
from datetime import datetime
import SimpleDocumentStore.PreValidations as preV


class File:
    def __init__(self, location):
        self.location = location

    def save_file(self, file_name, content):
        full_path = File(self.location).get_full_path(file_name)
        directory = os.path.dirname(full_path)
        if not os.path.exists(directory):
            os.makedirs(directory)
        f = open(full_path, 'w')
        try:
            f.write(str(content))
        except:
            raise
        finally:
            if f is not None:
                f.close()
        return full_path

    def open_file(self, file_name, mode):
        if preV.validate_mode(mode):
            return open(self.get_full_path(file_name), mode)

    def get_full_path(self, file_name):
        try:
            path = os.path.join(self.location, file_name)
        except:
            raise
        return os.path.normpath(path)

    def get_size(self, file_name):
        return os.path.getsize(self.get_full_path(file_name))

    def get_creation_time(self, file_name):
        return datetime.fromtimestamp(os.path.getctime(self.get_full_path(file_name)))

    def get_updated_time(self, file_name):
        return datetime.fromtimestamp(os.path.getmtime(self.get_full_path(file_name)))

    def delete_file(self, file_name):
        full_path = self.get_full_path(file_name)
        try:
            if os.path.exists(full_path):
                os.remove(full_path)
        except:
            raise
