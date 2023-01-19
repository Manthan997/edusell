import sqlite3
connection= sqlite3.connect('database.db')
with open('schema.sql') as f:
    connection.executescript(f.read())
connection.execute('PRAGMA foreign_keys = ON')
# does that even work?...let's print it
# val = (connection.execute('PRAGMA foreign_keys;'))
# print(val)
connection.commit()
connection.close()