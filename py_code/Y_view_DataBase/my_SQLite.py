import sqlite3, os

# conet = sqlite3.connect('test.db')
# cursor = conet.cursor()
# cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# cursor.execute('insert into user (id, name) values (\'1\', \'deathot\')')
# cursor.rowcount
# conet.commit()
# cursor.close()
# conet.close()

# conet = sqlite3.connect('test.db')
# cursor = conet.cursor()

# cursor.execute('select * from user where id = ?', ('1', ))
# values = cursor.fetchall()
# values
# cursor.close()
# conet.close()

#test
import os, sqlite3

db_file = os.path.join(os.path.dirname(__file__), 'test.db')
if os.path.isfile(db_file):
    os.remove(db_file)

# 初始数据:
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
conn.commit()
cursor.close()
conn.close()

def get_score_in(low, high):
    ' 返回指定分数区间的名字，按分数从低到高排序 '
    conn = sqlite3.connect('db_file')
    cursor = conn.cursor()
    cursor.execute('select * from user where score >= ? and score <= ?', (low, high))
    values = sorted(cursor.fetchall(), key = lambda x: x[2])
    list = [i[1] for i in values]    
    cursor.close()
    conn.close()
    return list

# 测试:
assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95)
assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100)
