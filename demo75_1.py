import sqlite3

connection = sqlite3.connect("demo75.sqlite")
print("db connected")
DROP_DDL = """
DROP TABLE IF EXISTS EMPLOYEE;
"""
CREATE_DDL = """
CREATE TABLE EMPLOYEE
(ID INTEGER PRIMARY KEY,
NAME TEXT NOT NULL,
AGE INT NOT NULL,
ADDRESS CHAR(50));
"""
connection.execute(DROP_DDL)
connection.execute(CREATE_DDL)
connection.close()
