import psycopg2
from psycopg2 import sql

def get_connection(data):
    khost, kuser, kpasswd, kdb = data.split('#')
    return psycopg2.connect(host=khost, user=kuser, password=kpasswd, dbname=kdb)

def find_data(db_str_postgres, table_name, query=None, values=None):
    conn = get_connection(db_str_postgres)
    cur = conn.cursor()
    if query:
        sql_query = sql.SQL("SELECT * FROM {} WHERE {}").format(sql.Identifier(table_name),sql.SQL(query))
        cur.execute(sql_query, values)
    else:
        sql_query = sql.SQL("SELECT * FROM {}").format(sql.Identifier(table_name))
        cur.execute(sql_query)
    res = cur.fetchall()
    return res

def insert_data(db_str_postgres, table_name, columns, values):
    conn = get_connection(db_str_postgres)
    cur = conn.cursor()
    sql_query = sql.SQL("INSERT INTO {} ({}) VALUES ({})").format(sql.Identifier(table_name),sql.SQL(', ').join(map(sql.Identifier, columns)),sql.SQL(', ').join(sql.Placeholder() * len(values)))
    cur.execute(sql_query, tuple(values))
    conn.commit()
    return "Inserted successfully"

def update_data(db_str_postgres, table_name, id_val, col, value):
    if not col or value is None:
        return "Column and value are required"
    conn = get_connection(db_str_postgres)
    cur = conn.cursor()
    set_clause = sql.SQL("{} = {}").format(sql.Identifier(col), sql.Placeholder())
    sql_query = sql.SQL("UPDATE {} SET {} WHERE id = %s").format(sql.Identifier(table_name), set_clause)
    combined_values = [value, id_val]
    cur.execute(sql_query, combined_values)
    conn.commit()
    return "Updated successfully"


def delete_data(db_str_postgres, table_name, query=None, values=None):
    if not query:
        return "Query is required"

    conn = get_connection(db_str_postgres)
    cur = conn.cursor()
    sql_query = sql.SQL("DELETE FROM {} WHERE {}").format(sql.Identifier(table_name),sql.SQL(query))
    cur.execute(sql_query, values)
    conn.commit()
    return "Deleted successfully"

if __name__ == '__main__':
    db_str_postgres = "localhost#postgres#PostGres32!@#test1"
    #insert_result = insert_data(db_str_postgres, "employees", {"name":"kavya","age":25})
    #insert_result = insert_data(db_str_postgres, "employees", ["name","age"],["durga",29])
    #print(insert_result)
    #find_result = find_data(db_str_postgres, "employees")
    #print( find_result)
    #update_result = update_data(db_str_postgres, "employees", "name=%s", {"name": "kavyabai"},"kavya")
    update_result = update_data(db_str_postgres, "employees", 8,"name", "kavyabairg")
    print( update_result)
    #delete_result = delete_data(db_str_postgres, "employees", "name= %s", ("kavya",))
