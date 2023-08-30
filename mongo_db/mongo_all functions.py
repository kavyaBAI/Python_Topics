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

