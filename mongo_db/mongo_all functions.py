#_________________________________________________________________________________________________
# list all subscription and without subscription where have to check if the sub is in the database,
#if it is present then list all the collections. and return it

def get_all_collection(db_str,collection,query):
    client,db_name  = createDbConn(db_str)
    db = client[db_name]
    matching_collections = []
    collection_names = db.list_collection_names()
    sub1, sub2  = get_sub(db_str,collection,query)
    for sub, without_sub in zip(sub1, sub2 ):
        substring = [sub, without_sub]
        collections_with_substring = [c for c in collection_names if any(sub in c for sub in substring)]
        matching_collections.extend(collections_with_substring)
    return matching_collections
#________________________________________________________________________________________________
# copying the collections from source_db to dest_db 
def dump_collections(matched_collections,db_str1,db_str2):
    source_client, source_db_name = createDbConn(db_str1)
    target_client, target_db_name = createDbConn(db_str2)

    source_db = source_client[source_db_name]
    target_db = target_client[target_db_name]
    for collection_name in matched_collections:
        source_collection = source_db[collection_name]
        target_collection = target_db[collection_name]

        documents_to_copy = source_collection.find({})
        documents_to_insert = []

        for document in documents_to_copy:
            # Exclude the _id field to generate new _id values
            del document['_id']  # thre will me same id for many collections we have to remove it 
            documents_to_insert.append(document)

        target_collection.insert_many(documents_to_insert)
    source_client.close()
    target_client.close()
#_____________________________________________________________________________________
#for every different collection insert the values 
#_______________________________________________________________________________________
# here for every collection insert the data ,if i do one by one insertion it will take time.so append all the data in the list
def get_customer_mysql2(db_str):
    conn, cursor = get_connection(db_str)
    #print(res)
    sql = "SELECT id , subscription_id FROM customer_subscription;"
    cursor.execute(sql)
    res1 = cursor.fetchall()
    st = time.time()
    for i, (idx, sub) in enumerate(res1):
        print(i, len(res1))
        sql = "SELECT * FROM customer_cost where subscription_id = %s"%idx
        cursor.execute(sql)
        res = cursor.fetchall()
        collection = sub.replace("-","")+"_cost"
        insertion_data = []
        del_list = []
        for [idx2,s_idx, cost, date_, curr] in res:
            date_part = date_.date()
            date_str = date_part.isoformat()
            data_dict = {"sub":sub , "cost" : cost , "cost_p": 0, "date":date_str , "currency": curr}
            insertion_data.append(data_dict)
            del_list.append(date_str)
        if insertion_data:
            query = {"date":{"$in":del_list}}
            export_data.deletedata(db_str1, collection, query)
            export_data.insertdata(db_str1, collection, insertion_data)
    cursor.close()
    conn.close()
    print(time.time()- st)
    return all_data
# in the below function i was inserting one by one wich was takin more for one collection to insert the data
def get_customer_mysql(db_str):
    conn, cursor = get_connection(db_str)
    sql = "SELECT * FROM customer_cost;"
    cursor.execute(sql)
    res = cursor.fetchall()
    #print(res)
    sql = "SELECT id , subscription_id FROM customer_subscription;"
    cursor.execute(sql)
    res1 = cursor.fetchall()
    subs_dict = {}
    for (idx, sub) in res1:
        subs_dict[idx] = sub
    res_dict = {}
    ls = []
    data_dict_ls = []
    for all_cost in res:
        dates2 = all_cost[3]
        #print(dates2)
        date_part = dates2.date()
        date_str = date_part.isoformat()
        sub_id = all_cost[1]
        subs = subs_dict.get(sub_id)
        res = subs.replace("-","")
        X = res+"_cost"
        collection = X
        data_dict = {"sub":subs , "cost" : all_cost[2] , "cost_p": 0, "date":date_str , "currency": all_cost[4]}
        all_data = export_data.insertdata(db_str1, collection, data_dict_list)
        print( data_dict_list)
    cursor.close()
    conn.close()
#__________________________________________________________________________________________________________________