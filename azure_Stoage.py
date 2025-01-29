# files and fileshare have differnt  structure have differnt directory structure 
# blob starogare differ from file staroge 
# in file staroge there is differnt hirachy,have file permission 
# blob stoagre have no hirachy ,it includes metadata
# #blob are simpley unstructred binary or text at the web endpoint 
# in blob we can massive amount of unstructured data 



#blob storage have 3 resources(this hoe blob is organizsed)


differnce between blob and base64:
blob is binary Data.while base64 will convert binary to text encoding and decoding for the transmission.


#reading files from  azurestraoge
from azure.storage.blob import BlobServiceClient
import base64
import time

account_name = "cqdatastore"
account_key = "6hobPnAJR+Zr/onJc4tCVy9UPyM82lJfXHB/hkypsTf6r4/9DkX6NKMHSF28aG8wRj8R0Wgs195r+ASt2zI/lA=="
connection_string = f"DefaultEndpointsProtocol=https;AccountName=cqdatastore;AccountKey={account_key};EndpointSuffix=core.windows.net"

blob_service_client = BlobServiceClient.from_connection_string(connection_string)

def read_blob_and_convert_to_base64(container_name, file_name):
    container_client = blob_service_client.get_container_client(container_name)
    print("container_client",container_client)
    print("file_name",file_name)
    blob_client = container_client.get_blob_client(file_name)
    if 1:
        download_stream = blob_client.download_blob()
        blob_bytes = download_stream.readall()
        encoded_string = base64.b64encode(blob_bytes).decode('utf-8')
        return encoded_string

    #except Exception as e:
        #print(f"Error while processing the blob: {e}")
        #return None


def get_file_for_page(data_dict):
    doc_id = data_dict.get("doc_id")
    page_number = data_dict.get("page_number")
    st = time.time()
    blob_name = f"data/TechiData/{doc_id}/oimages/{page_number}.jpg"
    print("blob_name",blob_name)
    container_name = "docs"
    base_64_img = read_blob_and_convert_to_base64(container_name, blob_name)
    print(time.time() - st)
    return {"base_64_img":base_64_img}

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
