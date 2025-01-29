#reading files from  azurestraoge
from azure.storage.blob import BlobServiceClient
import base64
import time

account_name = "cqdatastore"
account_key = "6hobPnAJR+Zr/onJc4tCVy9UPyM82lJfXHB/hkypsTf6r4/9DkX6NKMHSF28aG8wRj8R0Wgs195r+ASt2zI/lA=="
connection_string = f"DefaultEndpointsProtocol=https;AccountName=cqdatastore;AccountKey={account_key};EndpointSuffix=core.windows.net"

blob_service_client = BlobServiceClient.from_connection_string(connection_string)


def download_blob(blob_name, local_dir):
    """Download blobs from Azure storage."""
    if not os.path.exists(local_dir):
        os.makedirs(local_dir)

    container_client = blob_service_client.get_container_client(container_name)
    blob_list = container_client.list_blobs(name_starts_with=blob_name)

    for blob in blob_list:
        if blob.size:  # Check if the blob has content
            # Get a blob client for the specific blob
            blob_client = container_client.get_blob_client(blob.name)

            # Create the full local file path
            local_file_path = os.path.join(local_dir, os.path.basename(blob.name))

            # Download and save the blob
            download_stream = blob_client.download_blob()
            with open(local_file_path, "wb") as file:
                file.write(download_stream.readall())

            print(f"Downloaded {blob.name} to {local_file_path}")

blob_name = "/docs/data/TechiData/1234/"
local_path = "/docs/data/TechiData/1234/"