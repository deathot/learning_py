# class User(object):
#     def __init__(self, id, name):
#         self.id = id
#         self.name = name
        
# [
#     User('1', 'deathot'), 
#     User('2', 'jie'), 
#     User('3', 'tao')

# ]

from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(String(20), primary_key = True)
    name = Column(String(20))

engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/test')
DBSession = sessionmaker(bind = engine)

#SQLALchemy初始化， 并定义表的class -ORM
class FlorID(Base):
    __table__name = 'flor'
    id = Column(String(20), primary_key = True)
    name = Column(String(20))

#在ORM下， 在User表中添加对象
session = DBSession()
new_user = User(id = '5', name = 'ting')
session.add(new_user)
session.commit()
session.close()

#查询数据-User对象
session = DBSession()
user = session.query(User).filter(User.name == 'deathot').one()
print('type:', type(user))
print('id:', user.id)
session.close()

class User(Base):
    __tablename__ = 'user'
    
    id = Column(String(20), primary_key = True)
    name = Column(String(20))
    books = relationship('Book')
    
class Book(Base):
    __table__ = 'book'

    id = Column(String(20), primary_key = True)
    name = Column(String(20))
    user_id = Column(String(20), ForeignKey('user.id'))
    id = Column(String(20), primary_key = True)
    name = Column(String(20))