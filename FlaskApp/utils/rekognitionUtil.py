import boto3

def detect_labels(bucket, imagekey):
    client = boto3.client("rekognition")

    response = client.detect_labels(Image={
        "S3Object": {"Bucket" : bucket, "Name": imagekey}
    })

    all_labels = []

    if response and "Labels" in response:
        all_labels = [label["Name"] for label in response["Labels"] ]

    return all_labels

if __name__ == "__main__":
    pass
