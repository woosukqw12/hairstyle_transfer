import sqlite3


#basic setting:
conn = sqlite3.connect('test01.db') #create db_file

cur = conn.cursor()
cur.execute("CREATE TABLE test01 (num INTEGER, title TEXT)") #create table
conn.commit()

cur.execute("select * from test01")

#<<examples>>

#solo_data insert: cur.execute("insert into test01 values (1, "abcd~")")
#                  conn.commit()
#many_data insert: cur.executemany("insert into test01 values (?,?)", data)  이때 data = [ (1,'a'),(2,'b'),(3,'c') ] 의 형식
#                  conn.commit()

# <data select> 
#1.  cur.execute('select * from test01')
#	for row in cur:
#		print(row) 
#==> (1,'a')
#    (2,'b')
#    (3,'c')
#
#2.  cur.execute('select * from test01')
#	rows = cur.fetchall()
#	print(rows)
#==> [ (1,'a'),(2,'b'),(3,'c') ]

#update data: cur.execute("update test01 set title where num= '2'")
#			  conn.commit()

#delete data: cur.execute("delete from test01 where num= '2'")
#			  conn.commit()
'''
f_titles = open("craw.txt", 'r')
title_list = f_titles.readlines()
#print(title_list)
f_titles.close()
'''
with open("craw.txt", 'r') as f:
    a = f.readlines()
    #print(a)

a = ''.join(a)
#print(a)
a = a[1:len(a)-1]
a = a.split(',')
#crawlist 리스트로 받아오기

data = a

for i in range(len(a)):
    cur.execute("""INSERT INTO test01  VALUES(?, ?)""", (i+1, a[i]))
conn.commit()
cur.execute("select * from test01;")
#cur.fetchall()
