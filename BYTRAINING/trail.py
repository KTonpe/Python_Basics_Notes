import csv

# with open('emp.csv','w',newline="") as f:
#     wt = csv.writer(f)
#     wt.writerow(['emp_id','emp_name','emp_salary'])
#     wt.writerow([1001,'John',10000])
# print("Data written in csv file")

with open('emp.csv','r') as q:
    rd = csv.reader(q)
    for row in rd:
        for elements in row:
            print(elements,"\t",end=" ")
        print()