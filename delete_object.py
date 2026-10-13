from google.cloud import storage


def delete_blob(bucket_name, blob_name):
    """Deletes an object from the bucket."""

    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)

    blob.delete()

    print(f"Object '{blob_name}' deleted from bucket '{bucket_name}'.")


if __name__ == "__main__":
    bucket_name = "gcp-aimi-bwt-sanikak"
    blob_name = "hello.txt"  # Name of the file to delete

    delete_blob(bucket_name, blob_name)