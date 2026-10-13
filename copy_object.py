from google.cloud import storage


def copy_blob(bucket_name, source_blob_name, destination_blob_name):
    """Copies an object within the same bucket."""

    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)
    source_blob = bucket.blob(source_blob_name)

    bucket.copy_blob(source_blob, bucket, destination_blob_name)

    print(
        f"Object '{source_blob_name}' copied to '{destination_blob_name}' in bucket '{bucket_name}'."
    )


if __name__ == "__main__":
    bucket_name = "gcp-aimi-bwt-sanikak"
    source_blob_name = "hello.txt"
    destination_blob_name = "hello_copy.txt"

    copy_blob(bucket_name, source_blob_name, destination_blob_name)