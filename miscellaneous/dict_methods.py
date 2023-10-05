#____________________________________________________________________
# i have to return the output in the form of {"same-date":{"sub1":[],"sub2":[]}
# for that create sub dictinoary return those sub dict ,using update method in  the dictionary append the dict
    
def get_all_cost_gc(dbstring, collection_name, sub, date_list, userid):
    date = date_list[0]
    data_dict_list = mongo_dbapi.finddata(dbstring, collection_name, {"user_id": userid, "sub": sub, "date": date})
    res_dict = {}
    sub_dict = {}  
    cost = 0
    cost_p = 0
    currency = ''
    if sub:
        for data_dict in data_dict_list:
            cost += data_dict.get("cost", 0)
            cost_p += data_dict.get("cost_p", 0)
            currency = data_dict.get("currency", 0)
            subs = data_dict.get("sub", 0)
        sub_dict[sub] = [cost, cost_p, currency, "subscription"]
    return sub_dict
#it will return one by one dict to another function
def graph_click():
     final_dict = {}
    date = all_dates[0]
    for (sub, month_year) in itertools.product(*[subs, all_months_years]):
        sub_new = sub.replace("-", "")
        collection_name = f"{sub_new}_{month_year}_GC"
        temp_dict = mongo_methods.get_all_cost_gc(db_str_mongo, collection_name, sub, all_dates,userid)
        ## the sub_dict will come here using append method append those dict
        cust_data.update(temp_dict)
    final_dict[date] = cust_data
#_________________________________________________________________________________________________________

#{k:{k:v},{k:v}} dict of dict
ls_dict = {1:{"name":'a','val':2,"val3":'4'},
        2:{"name":'b',"val":5,"val3":4},1:{"name":'b',"val":5,"val3":4}}
res_dict = {}
for key, value in ls_dict.items():
    val = value.get('val')
    val3 = value.get("val3")
    key2 = value.get("name")
    if key not in res_dict:
        res_dict[key] = {}

    if key2 not in res_dict[key]:
        res_dict[key][key2] = [val, val3]
    else:
        res_dict[key][key2][0] += val
        res_dict[key][key2][1] += val3
#_____________________________________________________________________________________________
#we have key :[many values ]we want to fetch all the values
sub,resource_group,hostpool_type,location = hp_type_dict.get(hp,["","","",""])
ex:
ls = {'PROD_DESKTOP_UNDERWRITING':['123','cental','ret','09-87']}
sub,name,region,rg = ls.get('PROD_DESKTOP_UNDERWRITING',["","","",""])
print(sub)
#______________________________________________________________________________________
#we have 2ls of dict ls= [{}] ,ls2 = [{}] traverse one use get method and fetch the value if all the 3 values exist then only insert it
temp_data_list = [{}] 
res = [{}]
  for idx, temp_data_dict in enumerate(res):
        sub = temp_data_dict.get("sub")
        hp_name = temp_data_dict.get("hostpool_name")
        dname = temp_data_dict.get("desktop_name")
        if not temp_data_list[0].get(sub) and temp_data_list[0].get(hp_name) and temp_data_list[0].get(dname): #check all 3 condition if all 3 are present in another dict then it will insert
            mongo_dbapi.insertdata(db_str_mongo,"desktop_mgmt", temp_data_list)
            print(idx ,"Inserted")
        else:
            print(idx ,"not inserted",len(res))
#__________________________________________________________________________________________________________________________________
#we can composite key but cannot use it to fetch the data unless if its present the fiven format ex;
sub = 123
dbane= kavye
key = (suc,dname,hpname)
dict_ls = {}
dict_ls[key] = {k1:v1,k2:v2}
#when using get method to get the value unless the key in the composite form u can fetch it 
res = dict_ls.get(key)
#u will get the value
dict_ls = {"k1":"v1","k2":"v2"}
res = dict_ls.get("k","k2")
#will throw an error
#____________________________________________________________________________________________
#comparing the 2 dictionary to check wheather 2 dict are same or not 
def are_dicts_equal(dict1, dict2):
    if set(dict1.keys()) != set(dict2.keys()):
        return False

    for key in dict1:
        if dict1[key] != dict2[key]:
            return False
    return True
dict1 = {"data":[{'a': 1, 'b': 2, 'c': 3},{'a': 1, 'b': 2, 'c': 3}]}
dict2 = {"data":[{'b': 2, 'a': 1, 'c': 3},{'a': 1, 'b': 2, 'c': 3}]}
if are_dicts_equal(dict1, dict2):
    print("The dictionaries are the same.")
else:
    print("The dictionaries are different.")
#_____________________________________________________________________________________________________


