from pymongo import MongoClient
import time



def createDbConn(db_str):
    host, port, uname, pwd, dbname = db_str.split('&')
    client = MongoClient(host, int(port), username = uname, password = pwd, authSource='admin')
    return client, dbname

def insertdata(db_str, collection, data_dict_list):
    client, db = createDbConn(db_str)
    x = client[db][collection].insert_many(data_dict_list)
    client.close()
    print(x)
    return x.inserted_ids

def finddata(db_str,collection,query):
    client, db = createDbConn(db_str)
    x = client[db][collection].find(query)
    data_list=list(x)
    #print(data_list)
    client.close()
    return data_list

def updatedata(db_str, collection, query, new_upvalues):
    client, db = createDbConn(db_str)
    x=client[db][collection].update_one(query, {'$set': new_upvalues})
    updated_count = x.modified_count
    print(updated_count)
    client.close()
    return updated_count

def deletedata(db_str,collection,query):
    client,db = createDbConn(db_str)
    x = client[db][collection].delete_many(query)
    client.close()
    return

if __name__=='__main__':

    data_dict_list = [{"name":"prasad","age":43,"role":"student"},{ "name":"ipl", "age":78, "role":"softwaere", "certificate":"fullstack"}]
    db_str = "localhost&27017&root&admin@123&cq_icco_master"
