import mongo_methods_dump
import mongo_dbapi
import os
import json
from bson import ObjectId

tag_cred_dev = "68.154.36.146#27017#cq_user#User@123#cloud_optimal_prod"
tag_cred_prod = "192.168.1.9#27017#cq_user#User@123#cloud_optimal_prod"
def get_all_collections():
    all_collections = mongo_methods_dump.get_collections(tag_cred_prod)
    target_coll = ["07_2024"]
    for each in all_collections:
        if any(each.endswith(suffix) for suffix in target_coll):
            data_dict_list = mongo_methods_dump.get_collection_data(tag_cred_prod, each)
            if data_dict_list:
                mongo_dbapi.deletedata(tag_cred_dev, each, {})
                mongo_dbapi.insertdata(tag_cred_dev, each, data_dict_list)


if __name__ == "__main__":
    print(get_all_collections())
