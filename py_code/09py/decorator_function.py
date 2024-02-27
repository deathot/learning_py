# def now():
#     print('hello')
# f = now
# #print(f())
# n1 = now.__name__
# print(n1)
# n2 = f.__name__
# print(n2)

# def log(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#     return wrapper
# @log
# def now():
#     print('hello')

# import functools
# def log(text):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kw):
#             print('%s %s():' % (text, func.__name__))
#             return func(*args, **kw)
#         return wrapper
#     return decorator

# @log('hello')
# def now():
#     print('world')

#  test

import time, functools
# def metric(fn):
#     @functools.wraps(fn)
#     def wrapper(*args, **kw):
#         start_time = time.time()
#         result = fn(*args, **kw)
#         end_time = time.time()
#         print('%s executed in %s ms' % (fn.__name__, (end_time - start_time)*1000))
#         return result
#     return wrapper

# # 测试
# @metric
# def fast(x, y):
#     time.sleep(0.0012)
#     return x + y

# @metric
# def slow(x, y, z):
#     time.sleep(0.1234)
#     return x * y * z

# f = fast(11, 22)
# s = slow(11, 22, 33)
# if f != 33:
#     print('测试失败!')
# elif s != 7986:
#     print('测试失败!')

def log(arg = None):
    def decorator(func):
        functools.wraps
        def wrapper(*args, **kw):
            if not callable(arg):
                print(arg)
            print('begin call')
            func(*args, **kw)
            print('%s %s():' % (arg, func.__name__))
            print('end call')
        return wrapper
    if callable(arg):
        return decorator(arg)
    else:
        return decorator
    

@log('execute')
def f():
    print('1')
f()
