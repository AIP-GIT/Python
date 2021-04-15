import MyDb as db
db.conn.execute('''
                INSERT INTO COMPANY (ID,NAME,AGE,ADR,SAL)
                VALUES (100,'ABC',52,'HYD',2000.00)
''')

db.conn.execute('''
                INSERT INTO COMPANY (ID,NAME,AGE,ADR,SAL)
                VALUES (2,'PQR',51,'HYD1',2000.00)
''')

db.conn.execute('''
                INSERT INTO COMPANY (ID,NAME,AGE,ADR,SAL)
                VALUES (3,'XYZ',23,'HYD2',20012.00)
''')

db.conn.execute('''
                INSERT INTO COMPANY (ID,NAME,AGE,ADR,SAL)
                VALUES (4,'ABC',52,'HYD',200.00)
''')
print("Records inserted successfully!!")

db.conn.commit()
db.conn.close()