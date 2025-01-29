#add the data to azure straoge
#from azure.storage.blob import BlobServiceClient, ContainerClient
from azure.storage.blob import BlobServiceClient, ContainerClient

import os

connection_string = "DefaultEndpointsProtocol=https;AccountName=cqdatastore;AccountKey=6hobPnAJR+Zr/onJc4tCVy9UPyM82lJfXHB/hkypsTf6r4/9DkX6NKMHSF28aG8wRj8R0Wgs195r+ASt2zI/lA==;EndpointSuffix=core.windows.net"

blob_service_client = BlobServiceClient.from_connection_string(connection_string)

container_name = "docs"
container_client = blob_service_client.get_container_client(container_name)

# Create the container if it doesn't exist
try:
    container_client.create_container()
    print(f"Container '{container_name}' created successfully.")
except Exception as e:
    print(f"Container '{container_name}' already exists or another error occurred: {e}")

# Local path where the files are stored
local_file_path = r"/home/azureuser/docs"

def upload_files_from_directory(local_dir, container_client):
    # Loop through the directory structure recursively
    for root, dirs, files in os.walk(local_dir):
        for file_name in files:
            local_file = os.path.join(root, file_name)
            blob_name = os.path.relpath(local_file, local_dir)  # Keep the directory structure
            blob_client = container_client.get_blob_client(blob=blob_name)

            with open(local_file, "rb") as data:
                blob_client.upload_blob(data, overwrite=True)

            print(f"File '{blob_name}' uploaded successfully.")

# Upload files recursively from the directory
upload_files_from_directory(local_file_path, container_client)
