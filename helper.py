# helper.py

from google.cloud import storage

class GCSHelper:
    def __init__(self, bucket_name):
        self.bucket_name = bucket_name
        self.storage_client = storage.Client()

    def upload_file(self, local_file_path, destination_blob_name):
        """Uploads a file to the GCS bucket."""
        bucket = self.storage_client.bucket(self.bucket_name)
        blob = bucket.blob(destination_blob_name)

        blob.upload_from_filename(local_file_path)

        print(f"File {local_file_path} uploaded to {destination_blob_name} in bucket {self.bucket_name}")

    def download_file(self, source_blob_name, local_file_path):
        """Downloads a file from the GCS bucket."""
        bucket = self.storage_client.bucket(self.bucket_name)
        blob = bucket.blob(source_blob_name)

        blob.download_to_filename(local_file_path)

        print(f"File {source_blob_name} downloaded to {local_file_path} from bucket {self.bucket_name}")
