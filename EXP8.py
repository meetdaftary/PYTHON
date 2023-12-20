import mysql.connector
mydb = mysql.connector.connect(
 host = 'localhost',
 user = 'root',
 password = '',
 database='furniture1'
)
mycursor = mydb.cursor()

# mycursor.execute("create database furniture1")
# mycursor.execute("""show databases""")

# mycursor.execute("""create table cupboard(
#  id int not null,
#  name varchar(75) not null,
#  price float not null,
#  count int not null,
#  primary key(id)
# )""")

# sql = """insert into cupboard(id, name, price, count) values (%s, %s, %s, %s)"""
# val = [
#  (2, 'cb2', 15000, 5),
#  (3, 'cb3', 7000, 15),
#  (4, 'cb4', 20000, 3),
#  (5, 'cb5', 40000, 5)
# ]
# mycursor.executemany(sql, val)
# mydb.commit()
# print(mycursor.rowcount, 'record(s) inserted.')

# mycursor.execute("""delete from cupboard where name = 'cb3'""")
# mydb.commit()
# print(mycursor.rowcount, 'record(s) deleted.')

mycursor.execute("""select id,name from cupboard""")
for x in mycursor:
    print(x)

# mycursor.execute("update cupboard set price = 8500 where name = 'cb2'")
# mydb.commit()
# print(mycursor.rowcount, 'record(s) updated.')

# mycursor.execute("alter table cupboard add year int")
# mydb.commit()``

# sql="""select * from cupboard"""
# mycursor.execute(sql)

# for x in mycursor:
#     print(x)
