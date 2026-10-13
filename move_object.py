from google.cloud import storage


def move_blob(bucket_name, source_blob_name, destination_blob_name):
    """Moves an object to a new location in the same bucket."""

    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)
    source_blob = bucket.blob(source_blob_name)

    # Copy the object
    bucket.copy_blob(source_blob, bucket, destination_blob_name)

    # Delete the original object
    source_blob.delete()

    print(
        f"Object '{source_blob_name}' moved to '{destination_blob_name}' in bucket '{bucket_name}'."
    )


if __name__ == "__main__":
    bucket_name = "gcp-aimi-bwt-sanikak"
    source_blob_name = "hello.txt"
    destination_blob_name = "folder1/hello.txt"

    move_blob(bucket_name, source_blob_name, destination_blob_name)