import MyDb as db
cursor = db.conn.execute("SELECT ID,NAME,SAL FROM COMPANY")

print("ID".ljust(10),"NAME".ljust(10),"SAL".ljust(10))
print("-".ljust(30,"-"))
for row in cursor:
    print(str(row[0]).ljust(10),str(row[1]).ljust(10),str(row[2]).ljust(10))

db.conn.close()