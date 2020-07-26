import sqlite3
import pandas as pd 
import os

connection = sqlite3.connect("MLBdb.sqlite3")
cursor = connection.cursor()

q1 = '''select avg(HR), AB, salary , RBI, r , Tb 
from MLB_table
order by HR DESC ;'''

r1 = cursor.execute(q1)

print( r1.fetchall())

q2 = '''select avg(hr), AB, salary , RBI, r , Tb   
from mlb_table 
where salary > 15000000
order by HR DESC ;'''

r2 = cursor.execute(q2)
print(r2.fetchall())


q3 = '''select avg(hr), AB, salary , RBI, r , Tb   
from mlb_table 
where salary > 10000000 and salary < 15000000
order by HR DESC  ;'''
r3 = cursor.execute(q3)
print(r3.fetchall())

q4 = '''select avg(hr), AB, salary , RBI, r , Tb   
from mlb_table 
where salary > 5000000 and salary < 10000000
order by HR DESC ;'''

r4 = cursor.execute(q4)
print(r4.fetchall())

q5 = '''select avg(hr), AB, salary , RBI, r , Tb   
from mlb_table 
where salary > 1000000 and salary < 5000000
order by HR DESC ;'''
r5 = cursor.execute(q5)
print(r5.fetchall())

q6 = '''select avg(hr), AB, salary , RBI, r , Tb   
from mlb_table 
where salary > 300000 and salary < 1000000
order by HR DESC ;'''
r6 = cursor.execute(q6)
print(r6.fetchall())



