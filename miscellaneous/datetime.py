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
