import sqlite3
connection = sqlite3.connect("demo75.sqlite")
print("db connected")
connection.close()
