from google.cloud import storage


def upload_blob_from_memory(bucket_name, contents, destination_blob_name):
    """Uploads text to a blob in the bucket."""

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_string(contents)

    print(
        f"'{destination_blob_name}' with contents '{contents}' uploaded to bucket '{bucket_name}'."
    )


if __name__ == "__main__":
    bucket_name = "gcp-aimi-bwt-sanikak"
    contents = "Hello! This is my first file uploaded using Python."
    destination_blob_name = "hello.txt"

    upload_blob_from_memory(
        bucket_name,
        contents,
        destination_blob_name,
    )