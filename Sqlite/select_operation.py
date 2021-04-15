import MyDb as db
cursor = db.conn.execute("SELECT ID,NAME,SAL FROM COMPANY")

for row in cursor:
    print(row)

db.conn.close()