from generic_fun import CommonUtils
from rabbitmq_publisher_consumer import RabbitMQ
from mysql_db_manager_v2 import DbManager
import os,shutil,time, zipfile, datetime
#import tiff_to_pdf
import tiff_to_pdf2 as tiff_to_pdf
import hashlib
from azure.storage.blob import BlobServiceClient

class AddQue:
    def __init__(self,config_path):
        self.common_obj = CommonUtils()
        self.config = self.common_obj.read_yaml_file(config_path)
        self.message_q_obj = RabbitMQ(server_address=self.config['generic']['rabbit_mq']['server_address'],mq_port=self.config['generic']['rabbit_mq']['server_port'],user=self.config['generic']['rabbit_mq']['user'],pwd=self.config['generic']['rabbit_mq']['password'],exchange_name=self.config['generic']['rabbit_mq']['exchange_name'])
        self.db_obj = DbManager(config_path)
        self.connection_string = "DefaultEndpointsProtocol=https;AccountName=cqdatastore;AccountKey=6hobPnAJR+Zr/onJc4tCVy9UPyM82lJfXHB/hkypsTf6r4/9DkX6NKMHSF28aG8wRj8R0Wgs195r+ASt2zI/lA==;EndpointSuffix=core.windows.net"
        self.account_name = "cqdatastore"
        self.container_name = "docs"
        self.blob_service_client = BlobServiceClient.from_connection_string(self.connection_string)

    def add_queue(self,result,queue_name,batch_name = None, priority=0):
        #self.message_q_obj.connect()
        self.message_q_obj.declare_queue(queue_name,durablity=True)
        grand_total_pages = 0
        not_added_list = []
        added_list = []
        for idx,item in enumerate(result):
            send_dict ={}
            send_dict["pdf"] = f"/docs/data/TechiData/{item['id']}/input.pdf"
            send_dict["opath"] = "/docs/data/TechiData/"
            send_dict["debug"] = 1
            send_dict["thread_cnt"] = 4
            send_dict["docid"] = str(item['id'])
            # send_dict["pid"] = item["project_name"]
            send_dict["pid"] = "MRT"
            # send_dict["subs"] = item['subscription']
            send_dict["subs"] = "generic"
            send_dict["ocr"] = "1"
            send_dict["org_pdf"] = self.common_obj.find_file(item['docName'],os.path.join(send_dict["opath"],"input_folder", send_dict["pid"]))
            if not send_dict["org_pdf"]:
                not_added_id_info = {"id":item['id'],"reason":f"File {item['docName']} not found in the {send_dict['opath']}/input_folder/*."}
                not_added_list.append(not_added_id_info)
                continue
            send_dict["batch_name"] = item["batch_name"]
            doc_pages = self.common_obj.get_pdf_page_count(send_dict["org_pdf"])
            if  not doc_pages:
                not_added_id_info = {"id":item['id'],"reason":f"Not able to read the file {send_dict['org_pdf']}."}
                continue
            send_dict["total_pages"] = doc_pages
            send_dict["min_pages"] = min(5,doc_pages)
            send_dict["priority"] = priority
            grand_total_pages += doc_pages
            self.message_q_obj.publish_priorty(queue_name,str(send_dict), your_priority=priority)
            added_list.append(item['id'])
        #self.message_q_obj.disconnect()
        print("Grand total pages: ", grand_total_pages)
        return {"total_pages": grand_total_pages,"added_list":added_list,"not_added_list":not_added_list,"status": True}

    def extract_path_from_county(self,project_name,file_path):
        # Split the file path by "/"
        parts = file_path.split("/")
        # Find the index of the element containing "MRT"
        mrt_index = parts.index(project_name)
        # Extract the county and the rest of the path
        county_path = "/".join(parts[mrt_index+1:])
        return county_path

    def hot_file_process(self, data_dict):
        project_name = data_dict.get('project_name',"MRT")
        source_directory = f"/docs/hotfiles/{project_name}"
        destination_directory = f"/docs/data/TechiData/input_folder/{project_name}"
        bin_folder_dir = f"/docs/data/TechiData/bin_folder/{project_name}"

        # print("Scan after 10 seconds..")
        time.sleep(3)
        self.message_q_obj.connect()
        container_client = self.blob_service_client.get_container_client(self.container_name)
        blob_list = container_client.list_blobs(name_starts_with=source_directory)

        for blob in blob_list:
            blob_name = blob.name
            if blob_name.endswith('.zip'):
                county = blob_name.split("/")[-2]
                print(county)
                print(blob_name)
                extracted_files_only_pdf = self.extract_zip_file_to_temp_unzip(blob_name, destination_directory, county)
                print(extracted_files_only_pdf)
                data_for_add_queue_bulk = self.add_docs_to_db(extracted_files_only_pdf, data_dict)
                self.add_queue_bulk(data_for_add_queue_bulk, county)
                for files in extracted_files_only_pdf:
                    file_name = os.path.basename(files)
                    dir_name = os.path.join(destination_directory, county)
                    if os.path.exists(dir_name):
                        file_path = os.path.join(dir_name, file_name)
                        if os.path.exists(file_path):
                            os.remove(file_path)  # Delete the file
                            print(f"Deleted file: {file_path}")
                        else:
                            print(f"File not found: {file_path}")
                    else:
                        print(f"Directory not found: {dir_name}")
                #try:
                    #os.rmdir(os.path.join(destination_directory, county, "temp_unzip"))
                #except:
                    #print("directory could not be deleted, corrupt files.")
        self.message_q_obj.disconnect()
        return


    def create_directories(self,data_dict):
        project_name = data_dict.get('project_name',"MRT")
        county_list =  data_dict.get('county_list',[
            "FL_HILLSBOROUGH",
            "FL_VOLUSIA",
            "PA_PHIALDEPHIA",
            "TX_HARRIS",
            "TX_WILLIAMSON"
        ])
        source_directory = f"/docs/hotfiles/{project_name}"
        destination_directory = f"/docs/data/TechiData/input_folder/{project_name}"
        for county in county_list:
            os.makedirs(f"{source_directory}/{county}", exist_ok=True)
            os.makedirs(f"{destination_directory}/{county}", exist_ok=True)

    def add_files_to_queue(self,data_dict):
        queue_name = data_dict.get('queue_name',self.config['generic']['rabbit_mq']['queue_dict']['skew']['queue_name'])
        request_type = data_dict.get('request_type')
        input_data = data_dict.get('request_data')
        batch_name = data_dict.get('batch_name')

        db_output = self.db_obj.get_file_info_on_request_type(request_type,input_data)
        if not db_output:
            return {"status": False}
        result = self.add_queue(db_output,queue_name,batch_name = batch_name)
        return result

    def extract_zip_file(self, zip_file_path, destination_dir):
        print("zip_file_path", zip_file_path)
        print('destination_dir', destination_dir)
        extracted_files = []

        with zipfile.ZipFile(zip_file_path, 'r') as zip_file:
            for file_info in zip_file.infolist():
                if file_info.is_dir():
                    continue

                file_path = file_info.filename
                extracted_path = file_path.split('/')[-1]
                file_type = os.path.splitext(extracted_path)[-1]
                if file_type.lower() not in [".pdf", ".tif", ".tiff"]:
                    continue

                source_path = "/".join(zip_file_path.split("/")[:-1])
                extracted_path = os.path.join(source_path, extracted_path)
                with open(extracted_path, 'wb') as dst:
                    with zip_file.open(file_info, 'r') as src:
                        shutil.copyfileobj(src, dst)

        # avoid same name (otherwise we'll get shutil.Error: Destination path already exist)
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        file_name = zip_file_path.split("/")[-1].split(".")[0]
        rename_file = f"{destination_dir}/{file_name}_{timestamp}.zip"

        print('\nrename_file:', rename_file)
        shutil.move(zip_file_path, rename_file)

        #shutil.move(zip_file_path, destination_dir)

        return "Zip file extracted & moved successfully."

    def download_blob_to_local(self, blob_path, local_path):
        """
        Downloads a blob from the Azure storage to the local system.
        """
        blob_client = self.blob_service_client.get_blob_client(self.container_name,blob_path)
        with open(local_path, "wb") as file:
            file.write(blob_client.download_blob().readall())
        print(f"Downloaded {blob_path} to {local_path}")

    def upload_to_blob(self, blob_path, local_file_path):
        """
        Uploads a local file to the Azure blob storage.
        """
        print(blob_path,"blob_path","yyyyyyyyyyyyyyyyyyy")
        blob_client = self.blob_service_client.get_blob_client(self.container_name,blob_path)
        with open(local_file_path, "rb") as file:
            print(local_file_path,"999999999999999999999999")
            blob_client.upload_blob(file, overwrite=True)
        print(f"Uploaded {local_file_path} to {blob_path}")

    def extract_zip_file_to_temp_unzip(self, zip_file_path, destination_dir, county):
        print("zip_file_path", zip_file_path)
        destination_dir = os.path.join(destination_dir, county)
        os.makedirs(destination_dir, exist_ok=True)
        print('destination_dir', destination_dir)
        zip_file_name = os.path.basename(zip_file_path)
        moved_zip_file_path = os.path.join(destination_dir, zip_file_name)
        self.download_blob_to_local(zip_file_path, moved_zip_file_path)
        print(f"Downloaded zip file to: {moved_zip_file_path}")
        container_client = self.blob_service_client.get_container_client(self.container_name)
        blob_client = container_client.get_blob_client(zip_file_path)
        blob_client.delete_blob()
        print(f"Blob '{zip_file_path}' deleted successfully.")
        extracted_files = []
        temp_unzip_dir = os.path.join(destination_dir, "temp_unzip")
        os.makedirs(temp_unzip_dir, exist_ok=True)
        with zipfile.ZipFile(moved_zip_file_path, 'r') as zip_file:
            zip_file.extractall(temp_unzip_dir)
            print(f"Extracted all files to: {temp_unzip_dir}")
            # Process and upload the extracted files
            for file_name in os.listdir(temp_unzip_dir):
               print(file_name,"file_name")
               file_path = os.path.join(temp_unzip_dir, file_name)
               print(file_path,"file_path")
               new_file_name =  self.common_obj.add_under_score_and_timestamp(file_name)
               new_file_path =  os.path.join(temp_unzip_dir,new_file_name)
               shutil.move(file_path,new_file_path)
               file_type = os.path.splitext(file_name)[-1]
               if  file_name.lower().endswith('.pdf'):
                    self.upload_to_blob(f"/docs/data/TechiData/input_folder/MRT/{county}/{new_file_name}", new_file_path)
                    extracted_files.append(new_file_path)
                    print(f"Extracted: {file_path}")
               #elif file_name in [".tif", ".tiff"]:
               #elif ".tif" in file_name or ".tiff" in file_name:
               if file_name.lower().endswith('.tiff') or file_name.lower().endswith('.tif'):
                    tiff_to_pdf_file = self.convert_if_any_tiff_to_pdf(new_file_path)
                    print(tiff_to_pdf_file)
                    tiff_to_pdf_file_name = tiff_to_pdf_file.split("/")[-1]
                    print(tiff_to_pdf_file_name)
                    self.upload_to_blob(f"/docs/data/TechiData/input_folder/MRT/{county}/{tiff_to_pdf_file_name}", tiff_to_pdf_file)
                    extracted_files.append(tiff_to_pdf_file)
               else:
                    if os.path.isfile(file_path):
                        os.remove(file_path)
                        print(f"Deleted file: {file_path}")
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                        print(f"Deleted directory: {file_path}")

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        file_name = os.path.splitext(moved_zip_file_path)[0]
        print(file_name)
        rename_file_path = os.path.join(moved_zip_file_path, f"{file_name}_{timestamp}.zip")
        rename_file_name = f"{file_name}_{timestamp}.zip"
        shutil.move(moved_zip_file_path, rename_file_path)
        print(f"Renamed zip file to: {rename_file_name}")
        #blob_name = f"/docs/data/TechiData/input_folder/MRT/{county}/{new_rename_file}"
        self.upload_to_blob(rename_file_name,rename_file_path)
        os.remove(rename_file_path)
        print(rename_file_path,"rename_file_path")
        return extracted_files




    def convert_if_any_tiff_to_pdf(self,temp_file_path):
        pdf_list = []
        #for temp_file_path in extracted_files:
        if 1:
            if temp_file_path.lower().endswith('.tiff') or temp_file_path.lower().endswith('.tif'):
                print(f"Converting tiff to pdf: {temp_file_path}")
                print(f"Temp file path: {temp_file_path}")
                temp_file_path = tiff_to_pdf.tiff_to_pdf(temp_file_path)
                #pdf_list.append(temp_file_path)
                print(f"Converted to pdf: {temp_file_path}")
                return temp_file_path

            elif temp_file_path.lower().endswith('.pdf'):
                pdf_list.append(temp_file_path)

        return pdf_list

    def add_docs_to_db(self, extracted_files, data_dict):
        insert_data = []
        project_name = data_dict.get('project_name',"MRT")
        subscription = data_dict.get('subscription',"sub_mrt2")
        user_id = data_dict.get('user_id',110)
        publish = data_dict.get('publish',1)
        process_status = data_dict.get('process_status',1)

        for file_path in extracted_files:
            doc_name = os.path.basename(file_path)
            #doc_name = self.common_obj.add_under_score_and_timestamp(doc_name)
            county = os.path.basename(os.path.dirname(os.path.dirname(file_path)))
            doc_type = doc_name.split('.')[-1]
            dest_file_new = os.path.join(os.path.dirname(os.path.dirname(file_path)), doc_name)
            #dest_file_new = os.path.join(os.path.dirname(file_path), doc_name)

            with open(file_path, 'rb') as file_to_check:
                data = file_to_check.read()
                md5_returned = hashlib.md5(data).hexdigest()

            insert_data.append((user_id, doc_name, doc_type, publish, process_status, dest_file_new, project_name, subscription, county, md5_returned))
            shutil.move(file_path, dest_file_new)

        print(f"Insert data: {insert_data}")
        ids = self.db_obj.insert_files_batch(insert_data)

        print(f"id list from db: {ids}")
        return ids


    def add_queue_bulk(self, results, county):
        data_dict = {}
        data_dict["queue_name"] = "docprocessing-skew"
        data_dict["request_type"] = "doc_id_list"
        data_dict["priority"] = "10"
        data_dict["batch_name"] = county
        if len(results) == 1:
            results = results * 2
        data_dict["request_data"] = results
        res = self.add_files_to_queue(data_dict)


if __name__ == "__main__":
    start_time = time.time()
    obj = AddQue("../config_cp.yaml")
    data_dict = {
        "queue_name": "docprocessing-skew",
        "project_name": "MRT",
        "subscription": "sub_mrt2",
        "user_id": 110,
        "publish": 1,
        "process_status": 1
        }
    print("Scanning started")


    #obj.hot_file_process(data_dict)
    #print("Scanning finished")

    # finish_time = time.time()
    # print(f"Start to finish time: {finish_time - start_time}")

    while True:
        obj.hot_file_process(data_dict)
        print("Scanning...")
