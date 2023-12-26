# app.py

import sys
from helper import GCSHelper

def main():
    if len(sys.argv) != 2:
        print("Usage: python app.py <file_name>")
        sys.exit(1)

    file_name = sys.argv[1]
    bucket_name = "testing_bucket_2612"  # Replace with your GCS bucket name

    # Instantiate GCSHelper
    gcs_helper = GCSHelper(bucket_name)

    # Upload the file to GCS
    gcs_helper.upload_file(file_name, file_name)

    # Download the file from GCS
    download_path = f"downloaded_{file_name}"
    gcs_helper.download_file(file_name, download_path)

if __name__ == "__main__":
    main()
