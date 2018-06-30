from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='SimpleDocumentStore',
    version='0.1',
    description='A library to store the documents to the local file system and AWS S3',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='reetikaS',
    packages=['SimpleDocumentStore'],
    install_requires=[
          'boto3',
          'botocore'
      ],
    url="https://github.com/reetikaSR/SimpleDocumentStore",
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License"]
)
