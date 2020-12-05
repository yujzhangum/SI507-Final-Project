import sqlite3

DBNAME = 'FINAL507.sqlite'
connection = sqlite3.connect(DBNAME)

cursor = connection.cursor()
query = "CREATE TABLE JOB_FINAL3 (id int, position varchar(255), company varchar(255), location varchar(255), FOREIGN KEY (id) REFERENCES HIB (id_H1B))"
result = cursor.execute(query).fetchall()

query = "CREATE TABLE HIB4 (id_H1B int,time varchar(255), status varchar(255), salary varchar(255))"
result = cursor.execute(query).fetchall()
connection.close()