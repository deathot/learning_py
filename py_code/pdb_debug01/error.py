# def foo():
#     r = some_function()
#     if r == (-1):
#         return (-1)
#     return r

# def bar():
#     r = foo()
#     if r == (-1):
#         print('Error')
#     else:
#         pass

# try:
#     print('try')
#     r = 10 / 2
#     print('result:', r)
# except ZeroDivisionError as e:
#     print('except:', e)
# except ValueError as e:
#     print('ValueError:', e)
# else:
#     print('no error')
# finally:
#     print('finally')
# print('END')

# try:
#     foo()
# except ValueError as e:
#     print('ValueError')
# except UnicodeError as e:
#     print('UnicodeError')

# def foo(s):
#     return 10 / int(s)

# def bar(s):
#     return foo(s) * 2

# def main():
#     try:
#         bar('0')
#     except Exception as e:
#         print('Error:', e)
#     finally:
#         print('finally...')

# main()

#err.py:
# import logging

# def foo(s):
#     return 10 / int(s)

# def bar(s):
#     return foo(s) * 2

# def main():
#     try:
#         bar('0')
#     except Exception as e:
#         logging.exception(e)
# main()
# print('END')

#err_raise.py
# class FooError(ValueError):
#     pass

# def foo(s):
#     n = int(s)
#     if n == 0:
#         raise FooError('invalid value: %s' % s)
#     return 10 / n

# foo('0')

# def foo(s):
#     n = int(s)
#     if n == 0:
#         raise ValueError('invalid value: %s' % s)
#     return 10 / n

# def bar():
#     try:
#         foo('0')
#     except ValueError as e:
#         print('ValueError')
#         raise

# bar()

# try:
#     10 / 0
# except ZeroDivisionError:
#     raise ValueError('input error')

from functools import reduce

def str2num(s):
    
    try:
        return int(s)
    
    except ValueError:
        return float(s)

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main()


# from functools import reduce

# def str2num(s):

#     try:

#         return int(s)

#     except ValueError:

#         return float(s)

# def calc(exp):

#     ss = exp.split('+')

#     ns = map(str2num, ss)

#     return reduce(lambda acc, x: acc + x, ns)

# def main():

#     r = calc('100 + 200 + 345')

#     print('100 + 200 + 345 =', r)

#     r = calc('99 + 88 + 7.6')

#     print('99 + 88 + 7.6 =', r)

# main()