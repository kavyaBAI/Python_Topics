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


