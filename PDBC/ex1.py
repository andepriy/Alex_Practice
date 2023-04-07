import mysql.connector


db = mysql.connector.connect(host='localhost',user='root',password='root')

if db:
    print('connected succsfully')

else:
    print('unsuccessfully')

