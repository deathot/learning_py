from contextlib import closing
from contextlib import contextmanager
from urllib.request import urlopen

# try:
#     f = open('001.bmp', 'r')
#     f.read()
# finally:
#     if f:
#         f.close()

# with open('002.txt', 'r') as f:
#     f.read()

# class Query(object):

#     def __init__(self, name):
#         self.name = name
    
#     def __enter__(self):
#         print('Begin')
#         return self
    
#     def __exit__(self, exc_type, exc_value, traceback):
#         if exc_type:
#             print('Error')
#         else:
#             print('End')
        
#     def query(self):
#         print('Query info about %s...' % self.name)

# with Query('deathot') as q:
#     q.query()

# from contextlib import contextmanager

# class Query(object):
    
#     def __init__(self, name):
#         self.name = name

#     def query(self):
#         print('Query info about %s...' % self.name)

# contextmanager #@contextmanager这个decorator接受一个generator，用yield语句把with ... as var把变量输出出去，然后，with语句就可以正常地工作了：
# def create_query(name):
#     print('Begin')
#     q = Query(name)
#     yield q
#     print('End')

# with create_query('deathot') as q:
#     q.query()

# def tag(name):
#     print("<%s>" % name)
#     yield
#     print("</%s>" % name)
    
# with tag("h1"):
#     print("hello")
#     print("world")

# from contextlib import closing
# from urllib.request import urlopen    

with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        print(line)
    
@contextmanager
def closing (thing):
    try:
        yield thing
    finally:
        thing.close()