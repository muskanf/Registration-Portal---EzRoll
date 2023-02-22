import mysql.connector


# to connect to the mysql database
mydb = mysql.connector.connect(
    user='root',
    passwd='',  # your password
    database='ezroll',  # the database to connect to
    host='127.0.0.1',  # localhost
    allow_local_infile=1  # needed so can load local files
)

myc = mydb.cursor()  # myc name short for "my cursor"

# to execute a SQL query
myc.execute(
    "select title, TERM_DESC, CRN, BEGIN_TIME, END_TIME from classes where CRSE_NUM = '1672'  ")

#store the result
ans = myc.fetchall()

# Prints the result
for i in ans:
    print(i)
