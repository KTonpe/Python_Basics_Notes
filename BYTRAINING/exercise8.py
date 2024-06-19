import sqlite3

def get_db_connection(db_path):
    try:
        con = sqlite3.connect(db_path)
        return con
    except sqlite3.DatabaseError as e:
        print(e)
        return None

def execute_query(con, query, params=None, fetchall=True, executemany=False, rows=None):
    try:
        cursor = con.cursor()
        if executemany and rows:
            cursor.executemany(query, rows)
        else:
            cursor.execute(query, params or ())
        
        if fetchall:
            return cursor.fetchall()
        return cursor.fetchone()
    except sqlite3.DatabaseError as e:
        con.rollback()
        print(e)
        return None
    finally:
        cursor.close()


def understanding():
    db_path = r"BYTRAINING\data\tables.sqlite"
    con = get_db_connection(db_path)
    if not con:
        return

    query_create_table = 'create table if not exists product(pid int, pname varchar(10), price float)'
    query_insert_row = "insert into product values(1001, 'mouse', 300)"
    query_display_all = 'select * from product'

    execute_query(con, query_create_table, fetchall=False)
    execute_query(con, query_insert_row, fetchall=False)
    rows = execute_query(con, query_display_all)

    print(rows)
    con.commit()
    con.close()

def dynamic_inserting():
    db_path = r"BYTRAINING\data\tables.sqlite"
    con = get_db_connection(db_path)
    if not con:
        return

    pid = int(input("Enter pid: "))
    pname = input("Enter pname: ")
    price = float(input("Enter price: "))
    query_dynamic_insert = "insert into product values(?, ?, ?)"

    execute_query(con, query_dynamic_insert, params=(pid, pname, price), fetchall=False)
    con.commit()
    con.close()

def dynamic_update_in_record():
    db_path = r"BYTRAINING\data\tables.sqlite"
    con = get_db_connection(db_path)
    if not con:
        return

    pname = input("Enter pname: ")
    price = float(input("Enter price: "))
    pid = int(input("Enter pid: "))
    query_update = "update product set pname = ?, price = ? where pid = ?"

    execute_query(con, query_update, params=(pname, price, pid), fetchall=False)
    con.commit()
    con.close()

def display_table():
    db_path = r"BYTRAINING\data\tables.sqlite"
    con = get_db_connection(db_path)
    if not con:
        return

    query = "select * from product"
    rows = execute_query(con, query)

    for row in rows:
        print(f"Pid: {row[0]} || Pname: {row[1]} || Price: {row[2]}")

    con.commit()
    con.close()

def dynamic_delete_row():
    db_path = r"BYTRAINING\data\tables.sqlite"
    con = get_db_connection(db_path)
    if not con:
        return

    pid = int(input("Enter pid: "))
    query_delete = "delete from product where pid = ?"

    execute_query(con, query_delete, params=(pid,), fetchall=False)
    con.commit()
    con.close()

if __name__ == '__main__':
    display_table()
    dynamic_update_in_record()
    display_table()
    dynamic_delete_row()
    display_table()