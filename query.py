
import mysql.connector
# import mysql.connector
#create user 'user'@'%' identified by 'password'
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
print(mydb)
mycursor = mydb.cursor()

mycursor.execute("select * from kri_DB.fsds")

for i in mycursor:
    print(i)

mycursor.execute('select studentid , firstname, class from kri_DB.fsds')

for i in mycursor:
    print(i)

mycursor.execute('select * from kri_DB.fsds where studentid = 130 ')

for i in mycursor:
    print(i)

mycursor.execute('select * from kri_DB.fsds where studentid > 130 ')

for i in mycursor:
    print(i)

mycursor.execute("select * from kri_DB.fsds where firstname = 'shubham' and class = 'sql'")

for i in mycursor:
    print(i)

mycursor.execute("update kri_DB.fsds set firstname = 'ROSHAN' where studentid = 125 ")

# When you update some value or del or set the values than you have to call the commit() method 

mydb.commit()

# if someone is asking me to chenge the classname sql to MYSql 
mycursor.execute("update kri_DB.fsds set class = 'MYSql'")
mydb.commit()

# if i want to delete the data where last name is khan
mycursor.execute("delete from kri_DB.fsds where lastname = 'khan'  ")
mydb.commit()
# if i want to find the min value of my studentid data
mycursor.execute("select min(studentid) from kri_DB.fsds")
for i in mycursor:
    print(i)
# if i want to find the max value of my studentid data
mycursor.execute("select max(studentid) from kri_DB.fsds")
for i in mycursor:
    print(i)
# can you plz give me total number of record's that i have in mycursor
mycursor.execute("select count(*) from kri_DB.fsds")
for i in mycursor:
    print(i)
mycursor.execute("update kri_DB.fsds set class = 'MONGO_DB' where studentid between 124 and 129")
mydb.commit()
# what if i want to know how many record's we have with the perticuler class
# to do this we have to use a group BY 
mycursor.execute("select count(*)  ,class from kri_DB.fsds group by class")
for i in mycursor:
    print(i)

# if i want to drop anything whether it is a database or a table than use this 
#mycursor.execute('drop table kri_DB.fsds')