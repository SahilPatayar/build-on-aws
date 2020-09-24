import boto3

s3_client = boto3.client("s3")

def generate_presigned_urls(bucket, imageKey):
    # http://boto3.readthedocs.io/en/latest/guide/s3.html#generating-presigned-urls

    return s3_client.generate_presigned_url("get_object", Params={
        "Bucket": bucket, "Key" : imageKey
    })

def put_object(bucket, imageKey, imageBytes, contentType):
    s3_client.put_object(
        Bucket=bucket,
        Key=imageKey,
        Body=imageBytes,
        ContentType=contentType
    )

if __name__ == "__main__":
    pass