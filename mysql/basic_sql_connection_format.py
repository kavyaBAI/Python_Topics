import MySQLdb
#from config import db_str1
import mysql.connector



def get_connection(data):
    khost, kuser , kpasswd , kdb = data.split('#')
    conn = MySQLdb.connect(host= khost, user= kuser,passwd= kpasswd,db=kdb, charset="utf8")
    cur = conn.cursor()
    return conn, cur

def get_users(db_str_mysql):
    conn, cur = get_connection(db_str_mysql)
    sql = "select email  from login;"
    cur.execute(sql)
    res = cur.fetchall()
    cur.close()
    conn.close()
    return res

def insertuser(db_str_mysql,args):
    conn, cur = get_connection(db_str_mysql)
    sql = "insert into login (full_name,email,password)values('%s','%s','%s')"
    cur.execute(sql % (args[0],args[1],args[2]))
    conn.commit()
    cur.close()
    print("True")
    conn.close()
    return "inserted sucessfully"








# if __name__=='__main__':
   #db_str1="localhost#root#Kavya8787@#durga_task"
