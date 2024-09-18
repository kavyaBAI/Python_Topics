#the session_host_df(dataframe) will select the particular column called subscription_id and those subscription_id should be unique.and 
#store it in list  
subs = list(session_host_df.subscription_id.unique())
#------------------------------------------------------------------------------------------------
#this function will group all the subIid  
session_host_df.groupby('subscription_id')
filtered_df = df.groupby(['subscription_id', 'MachineName']).apply(lambda x: x.sort_values('CreatedDate')).reset_index(drop=True)
#----------------------------------------------------------------------------------------------
#here data is dataframe insted of res = len(data.index) we can directly give like this
    insert_data_dict = {}
    for i in data.index:                                   #iloc[will give complete row value]
        hostpool_name = data.loc[i, "desktopgroupname"]    # It's indexing a particular row i and column "desktopgroupname".
#-------------------------------------------------------------------------------------------
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

print(res_dict)
#-------------------------------------------------------------------------------------------
#we have df we want its index how we do it
   for index, row in df.iterrows():
        hp = row["DesktopGroupName"]
#___________________________________________________________________________________________
# when we read excel some fields will be null which nan but pandas dataframe
#consider as float and throw an error ,so to slove this lets check its its not nan method (pd.notna())
#which is not nan () method 
def read_excel():
  file_path = r"D:\newsetoftask\cq_mailcontacts.xlsx"
  df = pd.read_excel(file_path,usecols=["To: (Address)","CC: (Address)"])
  res = len(df.index)
  for i in range(res):
    value = df.iloc[i]
    to_email = value[0]
    cc_email = value[1]
    if pd.notna(to_email) or pd.notna(cc_email): #this method 
      emial_col1 = re.findall(r"[A-Za-z0-9._%+-]+"r"@[A-Za-z0-9.-]+"r"\.[A-Za-z]{2,4}", str(to_email)) 
      emial_col2 = re.findall(r"[A-Za-z0-9._%+-]+"r"@[A-Za-z0-9.-]+"r"\.[A-Za-z]{2,4}", str(cc_email))
      print(emial_col1 )
#____________________________________________________________________________________________________
           
