#creating the dictinaory passing it as an parmet to another function where excel file is created .
#direct sending the dict will consider as key as column and values as the rows this is one method.
import pandas as pd 

def create_excel(res_dict):
    file = pd.DataFrame([res_dict])
    file.to_excel("file.xlsx",index = False)
    return  "excel file created"

def export_excel(doc_id, res):
    res_dict  = {}
    res_dict["doc_id"] = doc_id
    for key,value in res.items():
        rows = value.get('rows')
        for i in rows:
            topic_name =  i.get('Topic Name')
            values = i.get('Value_ar')
            for j in values:
                final_value = j.get('Value')
                res_dict[topic_name] = final_value
    # print(res_dict)
    resp = create_excel(res_dict)
    return resp
#______________________________________________________________________________
#another method in which passif columns name and the value in the list
def create_excel(res):
    ls = []
    live_data = res[0]
    dev_data = res[1]
    for (date,sub),cost_l in live_data.items():
        cost_d = dev_data[(date,sub)]
        diff_cost = abs(cost_l -cost_d)
        ls.append([date,sub,cost_l,cost_d,diff_cost])
    headers = ['Date','Subscription','live-cost','dev-cost','cost-diff']
    data = pd.DataFrame(ls,columns = headers)
    data.to_excel("tatasteeloutput.xlsx" , index = False)
#_____________________________________________________________________
#when we create excel using pandas 
headers = ['Emails']
    data = pd.DataFrame(ls,columns = headers)
    data.to_excel("Emials_.xlsx" , index = False)
#ls = ['','','','','','','',] it will  take each index value as zero and inserted into it.
#ls can be ls = [(1),(2),(3),(4)]
#we face problem when we have mutilple valueslike [(1,2,3),(1,2),(1)] in tuple  the error we face is  :- ValueError: 1 columns passed, passed data had 3 columns
#so what we have to do in below  form 
ls=[(['1','2']),(['1','2','3'])] 
#ls = ['satishgrams@gmail.com'] we have this we want in (['satishgrams@gmail.com'])
#we use  tup_list1 = ([*ls],)
      
#_________________________________________________________________________________________
# in pandas to create excel we have 2 methods
#1.dict,2.list......
#dict= {k1:v1,k2:v2,k3:v3}here key will the column name and value will the row values
#dict= {k1:[1,2,4,5],k2:[2,34,56]}
#ls = [1,"kavya","87"] mention column names = [value1,value2,value3]
#in pandas data store in horizontal and vertical 
