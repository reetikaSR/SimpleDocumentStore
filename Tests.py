import unittest
import SimpleDocumentStore


class Tests(unittest.TestCase):
    bck_name = "bucket_name"
    local_path = "local_path"
    aws_access_key = "aws_access_key"
    aws_secret_key = "aws_secret_key"

    afsm = SimpleDocumentStore.create_storage_mode(local_path,
                                                   'aws',
                                                  aws_access_key,
                                                  aws_secret_key
                                                  )
    fsm = SimpleDocumentStore.create_storage_mode(local_path)

    def test_save_doc(self):
        Tests.afsm.save_document("test1.pdf", "test1", bucket_name=Tests.bck_name)
        Tests.fsm.save_document("test1.pdf", "test1")

    def test_open_doc(self):
        f = Tests.afsm.open_document("test1.pdf", 'r', bucket_name=Tests.bck_name)
        f.read()
        f = Tests.fsm.open_document("test1.pdf", 'r')
        f.read()

    def test_rename_doc(self):
        Tests.afsm.rename_document("test1", "test11", bucket_name=Tests.bck_name)
        Tests.fsm.rename_document("test1", "test11")

    def test_get_size(self):
        s3s = Tests.afsm.get_size("test11", bucket_name=Tests.bck_name)
        s = Tests.fsm.get_size("test11")

    def test_get_creation_time(self):
        s3s = Tests.afsm.get_creation_time("test11", bucket_name=Tests.bck_name)
        s = Tests.fsm.get_creation_time("test11")
        a = s

    def test_get_modified_time(self):
        s3s = Tests.afsm.get_updated_time("test11", bucket_name=Tests.bck_name)
        s = Tests.fsm.get_updated_time("test11")
        a = s