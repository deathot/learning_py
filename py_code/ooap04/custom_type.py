# class Student(object):
#     def __init__(self, name):
#         self.name = name
#     def __str__(self) -> str:
#         return 'Student object (name: %s)' % self.name
#     __repr__ = __str__

# # print(Student('deathot'))
# s = Student('deathot')
# print(s)

# class Fib(object):
#     def __init__(self):
#         self.a, self.b = 0, 1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         self.a, self.b = self.b, self.a + self.b
#         if self.a > 100000:
#             raise StopIteration
#         return self.a
    
# for n in Fib():
#     print(n)

# class Fib(object):
#     def __getitem__(self, n):
#         a, b = 1, 1
#         if isinstance(n, int):
#             for x in range(n):
#                 a, b = b, a + b
#             return a
#         if isinstance(n, slice):
#             start = n.start
#             stop = n.stop
#             if start is None:
#                 start = 0
#             a, b = 1, 1
#             L = []
#             for x in range(stop):
#                 if x >= start:
#                     L.append(a)
#                     a, b = b , a+b
#                 return L

# Fib()[5]

# from typing import Any


# class Student(object):
#     def __init__(self):
#         self.name = 'deathot'

#     def __getattr__(self, attr):
#         if attr == 'score':
#             return 100
#         if attr == 'age':
#             return lambda: 21
#         raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
        

# s = Student()
# print(s.name)
# print(s.score)
# print(s.age())
# s.abc

# class Chain(object):

#     def __init__(self, path = ''):
#         self._path = path
    
#     def __getattr__(self, path):
#         return Chain('%s/%s' % (self._path, path))
    
#     def __call__(self, user):
#         return Chain('%s/%s' % (self._path, user))   
    
#     def __str__(self):
#         return self._path
    
#     __repr__ = __str__
# print(Chain().status.users('deathot').repos)
    

