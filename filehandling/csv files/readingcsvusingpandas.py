pandas is a open source libaray for the python 
dataframe can be created by readinf csv_file,excel_file,sqldatabase, list , dict or [{},{},{}]
to  read any file :

import pandas as pd 

df1 = pd.read_csv("fathname",usecols="[]")
after this find thye length
max_len = len(df.index)
for data in max_len:
  res  = df1.iloc[data]
#________________________________________________________________________________________________________
#reading 2 csv files and storing it values in sepearte dict and getting the di
# fference of 2 dict and return into csv file .
df = pd.read_csv()
df1 = pd.read_csv()

res_dict={}
res_dict1={}
res={}
resdict={}

max_row1=len(df.index)
max_row2=len(df1.index)
for i in range(max_row1):
    row1=df.iloc[i]
    #print(row1[1])
    if row1[1] not in res_dict:
        res_dict[row1[1]] = row1[0]
    else:
        res_dict[row1[1]]+=(row1[0])
#print(res_dict) 
for i in range(max_row2):
    row2=df1.iloc[i]
    #print(row1[1])
   #counting values row by row 
    if row2[1] not in res_dict1:
        res_dict1[row2[1]] = row2[0]
    else:
        res_dict1[row2[1]]+=(row2[0])
for i in res_dict1:
    if i in res_dict:
        diff=res_dict[i]-res_dict1[i]
        res[i]=diff
for i in res_dict1:
 
 #converting dataframe file to csv file 
    resdict[i]=[i,res_dict[i],res_dict1[i],res[i]]
    # headers=['date','till14', 'till8', 'diff']
#print(resdict)
headers=['date','till14', 'till8', 'diff']
data = pd.DataFrame(resdict.values(),columns=headers)
data.to_csv("output.csv", index=False) 
#____________________________________________________________________________________ 