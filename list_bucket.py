from google.cloud import storage


def list_buckets_with_partial_success():
    """Lists buckets and includes unreachable buckets in the response."""

    storage_client = storage.Client()

    buckets_iterator = storage_client.list_buckets(
        return_partial_success=True
    )

    for page in buckets_iterator.pages:
        if page.unreachable:
            print("Unreachable locations in this page:")
            for location in page.unreachable:
                print(location)

        print("Reachable buckets in this page:")
        for bucket in page:
            print(bucket.name)


# Call the function
if __name__ == "__main__":
    list_buckets_with_partial_success()