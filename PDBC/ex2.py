+import mysql.connector


db = mysql.connector.connect(host='localhost',user='root',password='root')

C1 = db.cursor()
C1.execute('show databases')

for i in C1:
    print(i)


('bird',)
# ('cat',)
# ('hospital',)
# ('information_schema',)
# ('mysql',)
# ('performance_schema',)
# ('saw',)
# ('sys',)

