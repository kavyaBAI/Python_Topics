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

