# import statement will open the database connection
import MyDb as db

# Execute the query
db.conn.execute('''
                CREATE TABLE COMPANY
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         AGE            INT     NOT NULL,
         ADR        CHAR(50),
         SAL         REAL);''')

print("Table created successfully!!")

# close the connection
db.conn.close()