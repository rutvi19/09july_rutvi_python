import sqlite3

try:
    sqlite3.connect("NEW.db")
    print("Database created and Successfully Connected to SQLite")
except Exception as e:
    print("Failed to connect to database")
    print(e)

 #table creation
# tb1_create = '''CREATE TABLE NEW(id int primary key not null,Name TEXT,address char(50))'''    
# try:
#     conn = sqlite3.connect("NEW.db")
#     cursor = conn.cursor()
#     cursor.execute(tb1_create)
#     print("Table created successfully")
# except Exception as e:
#     print(e)

# #insert data
# tb1_insert = '''INSERT INTO NEW(id,Name,address) VALUES(1,'John','California')'''
# try:
#     conn = sqlite3.connect("NEW.db")
#     cursor = conn.cursor()
#     cursor.execute(tb1_insert)
#     conn.commit()
#     print("Record inserted successfully")
# except Exception as e:
#     print(e)

#update data
tb1_update = '''UPDATE NEW(id,Name,address) VALUES(1,'rutvi','rajkot')'''
try:
    conn = sqlite3.connect("NEW.db")
    cursor = conn.cursor()
    cursor.execute(tb1_update)
    conn.commit()
    print("Record updated successfully")
except Exception as e:
    print(e)