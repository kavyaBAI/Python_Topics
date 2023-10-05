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