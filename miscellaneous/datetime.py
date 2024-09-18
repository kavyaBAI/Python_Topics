#_______________________________________________________________________________________________
#the dates are stored in the database . taking today now() we have to get the difference of 2 times in minute and hours.

def get_user_id(cred_id):
    conn,cur = get_connection(db_connection)
    sql = "select  * from log_table where cred_id = %s;"
    cur.execute(sql%(cred_id))
    res = cur.fetchall()
    print(res)
    datetime2 = datetime.datetime.now()
    for values in res:
        datetime1 = values[3]
        time_difference = datetime2 - datetime1
        diff_minutes = time_difference.total_seconds() / 60
        diff_hours = time_difference.total_seconds() / 3600
        if 'hostpool' ==  values[2]and math.ceil(abs(diff_minutes))< 6:
        pass
        elif 'cost' == values[2]  and  abs(diff_hours)< 4:
        pass
    cur.close()
    conn.close()
#________________________________________________________________________________________________
#in the sql the date will in the datetime object .have to convert datetimeobject to string 
from datetime import datetime, date

  for all_cost,all_subs in zip(res,res1):
        dates2 = all_cost[3]  # holds the date datetime.datetime(yyyy-mm-dd-)
        #print(dates2)
        date_part = dates2.date()
        date_str = date_part.isoformat()
#_______________________________________________________________________________

# converting string to dattimeobject 
from datetime import datetime

date_string = "2023-08-28 10:30:00"
format_string = "%Y-%m-%d %H:%M:%S"

datetime_object = datetime.strptime(date_string, format_string)
#________________________________________________________________________________-
#if u want to add the hours, min sec date to another dattimeobject then use time delta 
end_date = start_date + timedelta(hours=6)
#here we have start time and end time we have to add 5 min to each start_time ...then till  we reach end time .
 while start_time <=end_time:
            date_ = start_time.strftime("%d-%m-%Y")
            hour = start_time.strftime("%H")
            minute = start_time.strftime("%M")
            start_time+= timedelta(minutes=5)
#_________________________________________________________________________________________________________
 start_datetime = start_datetime.rstrip('Z')  # Remove 'Z' character from the end of the string
#-----------------------------------------------------------------------------------------------------
#if we want to get the total number of days then we can use the below method
from datetime import date
date1 = date(2018, 12, 13)
date2 = date(2015, 2, 25)
all_dates = (date1 -date2).days
print(all_dates)
##__________________________________________-
#['26.Oct.2023-02.Nov.2023', '18.Oct.2023-25.Oct.2023', '10.Oct.2023-17.Oct.2023', '02.Oct.2023-09.Oct.2023']
#if we want output like this take start_date and end_date 
from datetime import datetime,date,timedelta 
start_date = date.today() - timedelta(days=1)
end_date= start_date - timedelta(days=30)
result_dates = []
st,end = start_date, start_date
while start_date >= end_date:
    start_date -= timedelta(days=8)
    if start_date!= st:
        cur_date = start_date-timedelta(days=-1)
        st = cur_date
        d1 = st.strftime('%Y-%m-%d')
        short_month = st.strftime("%b")
        y,m,d = d1.split("-")
        date1 = "%s.%s.%s"%(d,short_month,y)
        d2 = end.strftime('%Y-%m-%d')
        short_month = end.strftime("%b")
        y,m,d = d2.split("-")
        date2 = "%s.%s.%s"%(d,short_month,y)
        result_dates.append(date1+"-"+date2)
        end = start_date
print(result_dates)
#___________________________________________________________________________________________________________________________
#to get the present time 
 t1 = time.time()
#______________________________________________________________________________
#Getting the 12hour format and 24 hour format
#The datetime module in Python doesn't inherently distinguish between 12-hour and 24-hour formats
#  when dealing with time. It depends on how you parse the input string and how you format it. 
from datetime import datetime

# Example time string in 12-hour format
time_string_12_hour = '08:30:45 PM'

# Example time string in 24-hour format
time_string_24_hour = '20:30:45'

# Parse the 12-hour format time string
t_12_hour = datetime.strptime(time_string_12_hour, '%I:%M:%S %p')
#________________________________________________________________-
from datetime import datetime,date,timedelta 
start_date = "17-11-2023"
ens_date = "14-12-2023"
st_date = datetime.strptime(start_date, "%d-%m-%Y")
end_dtate = datetime.strptime(ens_date, "%d-%m-%Y")
ls = []
st = st_date
while st_date <= end_dtate:
    st_date += timedelta(days=1)
    st = st_date
    date_ = date.isoformat(st_date)
    ls.append(date_)
print(ls)
#__________________________________________________________
from datetime import datetime,date,timedelta
start_date = date.today() - timedelta(days=1)
end_date= start_date - timedelta(days=30)
result_dates = []
st,end = start_date, start_date
while start_date >= end_date:
    start_date -= timedelta(days=8)
    if start_date!= st:
        cur_date = start_date-timedelta(days=-1)
        st = cur_date
        d1 = st.strftime('%Y-%m-%d')
        short_month = st.strftime("%b")
        y,m,d = d1.split("-")
        date1 = "%s.%s.%s"%(d,short_month,y)
        d2 = end.strftime('%Y-%m-%d')
        short_month = end.strftime("%b")
        y,m,d = d2.split("-")
        date2 = "%s.%s.%s"%(d,short_month,y)
        result_dates.append(date1+"-"+date2)
        end = start_date
print(result_dates)
#__________________________________________________________________
#output :-['24-01-04', '24-01-03', '24-01-02', '24-01-01', '23-12-31', '23-12-30', '23-12-29'] 
from datetime import datetime,date,timedelta

today_ = datetime.now()
list_dates = [today_ - timedelta(i) for i in range(7)]
y_m_d = [datetime.strftime(i,"%y-%m-%d")for i in list_dates]
print(y_m_d)
#_______________________________________________--
#input :- "2024/02/04"
#output :;"2024/2/4"
from  datetime import datetime
x = datetime.now()
yx = x.strftime('X%d/X%m/%Y').replace('X0','X').replace('X','')
print(yx)
#_________________________________________________________________--