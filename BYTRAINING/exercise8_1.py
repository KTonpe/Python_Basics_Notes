"""
create a file as deptData.csv
containing id,postion,location and add data
"""
import csv
from exercise8 import get_db_connection,execute_query

db_path = r"C:\Users\1038589\OneDrive - Blue Yonder\Desktop\Training Sessions\BYTRAINING\data\mydb.sqlite"
conn = get_db_connection(db_path)
cursor =conn.cursor()

def create_a_csv():
    try:
        entries_number = int(input("Enter number of entries : "))
    except ValueError as ve:
        print(f"An unexpected error occurred: {ve}")
    try:
        with open(r'BYTRAINING\deptData.csv','w',newline='') as file:
            wt = csv.writer(file)
            for _ in range(entries_number):
                id = input("Enter id : ")
                position = input("Enter position : ")
                location = input("Enter location : ")
                wt.writerow([id,position,location])
        print("Data added successfully")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
def create_table_to_databse():
    try:
        query = "CREATE TABLE IF NOT EXISTS dept (deptno varchar(50),position varchar(50),loc varchar(50))"
        cursor.execute(query)
        print("Table created successfully")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
def post_data_from_deptData_to_mydb():
    try:
        with open(r'BYTRAINING\deptData.csv','r') as file:
            query = "INSERT INTO dept VALUES (?,?,?)"
            rd = csv.reader(file)
            for row in rd:
                cursor.execute(query,row)
                conn.commit()
            print("Data added successfully")
    except Exception as e:
        conn.rollback()
        print(f"An unexpected error occurred: {e}")

def dislay_the_data_from_database():
    try:
        query = "SELECT * FROM dept"
        result = execute_query(con=conn,query=query,fetchall=True)
        for row in result:
            print(row)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ =="__main__":
    # create_a_csv()
    # create_table_to_databse()
    # post_data_from_deptData_to_mydb()
    dislay_the_data_from_database()