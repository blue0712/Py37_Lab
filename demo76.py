import sqlite3

connection = sqlite3.connect("demo76.sqlite")
print("db connected")
DROP_AND_CREATE_DDL = """
DROP TABLE IF EXISTS EMPLOYEE;
CREATE TABLE EMPLOYEE
(ID INTEGER PRIMARY KEY,
NAME TEXT NOT NULL,
AGE INT NOT NULL,
ADDRESS CHAR(50));
"""

connection.executescript(DROP_AND_CREATE_DDL)

connection.close()
