import logging
import boto3
from botocore.exceptions import ClientError

#Basic I/O for S3 buckets

def write_aws(bucket, key, content):
	return boto3.resource("s3").Object(bucket_name = bucket, key = key).put(Body = content)

def read_aws(bucket, key):
	return boto3.resource("s3").Object(bucket_name = bucket, key = key).get()["Body"].read().decode("utf-8")

def update_aws(bucket, key, content):
	try:
		old_content = read_aws(bucket, key)
	except ClientError:
		old_content = ""

	write_aws(bucket, key, old_content + "\n" + content)

#Logger which writes logs to S3 bucket

class S3Handler(logging.Handler):
	'''
	Warning: do not attach this handler to the root logger.  The problem is that the boto3 package itself
	uses the root logger, so the emit function triggers an infinite recursive loop.
	'''
	def __init__(self, bucket, filename):
		super().__init__()
		self.bucket = bucket 
		self.filename = filename

	def emit(self, record):
		update_aws(self.bucket, self.filename, self.format(record))