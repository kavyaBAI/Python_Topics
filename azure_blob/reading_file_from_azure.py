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