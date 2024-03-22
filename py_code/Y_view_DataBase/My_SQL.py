#创建mysql中名为test的数据库

import mysql.connector

connection = mysql.connector.connect(
    host = "localhost", 
    user = "root", 
    password = "password", 
)

cursor = connection.cursor()
cursor.execute("CREATE DATABASE test;")
connection.commit()
cursor.close()
connection.close()

#连接已有数据库test

import mysql.connector

conn = mysql.connector.connect(user = 'root', password = 'password', database = 'test')
cursor = conn.cursor()
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'deathot'])
cursor.rowcount
conn.commit()
cursor.close()
cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ('1', ))
values = cursor.fetchall()
values
cursor.close()
conn.close()