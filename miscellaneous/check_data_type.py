#we have to check the data types if thr same datatype add the cost values
def check_cost(tdata):
    c = 0
    for k, v in tdata[0].items():
        if 'Total' == k:continue
        if isinstance(v, float):    #using isinstance
            c += v
    print(c)
if __name__ == '__main__':
    tdata = [
    {
 "Total": 9783.48,
        "Total_Curr": "INR",
        "Total_P": "microsoft.compute",
        "abmf_to_anuntamum": 1.672772727275684,
        "abmf_to_anuntamum_Curr": "INR",
        "abmf_to_anuntamum_P": "microsoft.network",
        "abmfanuntavpngw": 379.52309999999943}]
#__________________________________________________________
def two_dict_cost(csv_dict,res_dict,cust_name):
    cost_ls = []
    cost_p_ls = []
    for (sub,date),[cost1,cost_p1] in res_dict.items():
        if not isinstance(csv_dict.get((sub,date)),float):if 
            print('patner cost')
            cost2 = csv_dict.get((sub,date))[0]
            cost_p2 = csv_dict.get((sub,date))[1]
            cost_diff = abs(cost1 - cost2)
            cost_p_diff = abs(cost_p1- cost_p2)
            if  cost_p_diff >1 or cost_diff>1:
                print(cost_p_diff)
                if cost_p_diff>1:
                    cost_p_ls.append((sub,date,cust_name))
                else:
                    cost_ls.append((sub,date,cust_name))
#___________________________________________________________________