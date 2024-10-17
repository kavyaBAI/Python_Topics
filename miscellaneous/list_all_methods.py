#we have to append to the same_dict if the sub is same in a 2darray format  
for all_sub in sub:
            if not  res_dict.get(all_sub):
                res_dict[all_sub] = [[i.get('regions'),i.get('resource_provider'),i.get('domains'),i.get('tags'),i.get('cust')]]
            else:
                res_dict[all_sub].append([i.get('regions'),i.get('resource_provider'),i.get('domains'),i.get('tags'),i.get('cust')])
    return res_dict
#_______________________________________________________________________________________________________
#we have to check the condition in a string i sub part of the string we use slice 
def resd_files():
    ls = []
    path = '/home/azureuser/mongo_data_insert/csv_files'
    lis_files = os.listdir(path)
    t_day = datetime.today()
    yest_day = t_day -timedelta(days =1)
    str_day = date.isoformat(yest_day)
    yes_day = str_day+".csv"
    for res in lis_files:
        date_for = res[-14:]
        if yes_day == date_for:
            ls.append(res)
    return ls

 #_____________________________________________________
#if u want to check wheater the list is empty or not. then we can use many method
#1. len() 
# 2if ls is'None'
#______________________________________
# #if u want to know the  len of the dictionary 
if not dict.get('name'):
     pass
#then the value is not present in that dictinary that key is not there 
#----------------------------------------------------------------------
#simple example 
#input :- ls [1,2]
#output :- ls[1,2,3]
ls.append(sum(ls))
#___________________________________________________________________
#i have ls1 = [(fd_id,fd_name),(),()]
ls2 = [(fd_id,file_count),()]
ls1_dict = {id_:name for id_,name in ls1}
final_list = [[ls1_dict[fd_id],fi_count,fd_id]for fd_id,fi_count in ls2]









 