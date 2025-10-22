import os
import socket

def public_s3_url(bucket, region, key):
    # URL de objeto público en S3
    return f"https://{bucket}.s3.{region}.amazonaws.com/{key}"

def container_id():
    # El hostname del contenedor suele ser el ID corto
    return socket.gethostname()
