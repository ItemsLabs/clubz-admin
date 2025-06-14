import boto3

from django.conf import settings


def upload_file(bucket, name, data, content_type):
    s3 = boto3.resource(
        's3',
        region_name='ams3',
        endpoint_url='https://ams3.digitaloceanspaces.com',
        aws_access_key_id=settings.DO_SPACE_API_KEY,
        aws_secret_access_key=settings.DO_SPACE_API_SECRET,
    )
    s3.Object(bucket, name).put(Body=data, ACL='public-read', ContentType=content_type)
    return get_file_url(bucket, name)


def get_file_url(bucket, name):
    return f"https://{bucket}.ams3.digitaloceanspaces.com/{name}"
