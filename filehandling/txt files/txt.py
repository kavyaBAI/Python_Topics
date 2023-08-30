def cust_cost():
    #res_dict = {}
    res1 ={}
    file_path =r"D:\Python\Python_Topics\filehandling\txt files\file.txt"
    res_dict = {}
    with open (file_path) as file:
        for line in file:
            res = line.split()   
            val = (res[0],res[1])
            if val not in res_dict:
                res_dict[val] = res[2]
               
            else:
                res_dict[val] += res[2] 
        print(res_dict)           
           
           
cust_cost()         