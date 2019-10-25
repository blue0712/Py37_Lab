import sqlite3
import time

connection = sqlite3.connect("demo76.sqlite")
print("db connected")
employees = [
    {'Name': 'Mark', 'Age': 43, 'Dept': 1, 'Addr': 'Taipei'},
    {'Name': 'John', 'Age': 38, 'Dept': 2, 'Addr': 'Taipei'},
    {'Name': 'Tim', 'Age': 35, 'Dept': 1, 'Addr': 'Hsinchu'},
    {'Name': 'Ken', 'Age': 49, 'Dept': 2, 'Addr': 'Taichung'},
]

DML1 = "INSERT INTO EMPLOYEE (NAME, AGE, ADDRESS) VALUES(?,?,?)"
startTime = time.time()
for j in range(1000):
    for e in employees:
        connection.execute(DML1, (e['Name'], e['Age'], e['Addr']));
        connection.commit()  # 4000 records, 4000commits
    #connection.commit() # 4000 records, 1000commits
connection.commit() # 4000 records, 1 commit
connection.close()
endTime = time.time()
delta = endTime - startTime
print(delta)
