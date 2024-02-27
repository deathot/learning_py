from functools import reduce

# a = abs(-1)
# print(a)

# b = abs
# print(b)

# c = b(-1)
# print(b)

# def add(x, y, b):
#     return b(x) + b(y)
# print(add(1, -2, abs))



# map/reduce function
# def f(x):
#     return x * x
# r = map(f, [1, 2, 3 , 4, 5])
# list(r)

# L = []
# for i in [1, 2, 3, 4, 5]:
#     L.append(f(i))
# print(L)

# list(map(str, [1, 2, 3, 4, 5]))

# reduce funciton
# def add(x, y):
#     return x + y
# reduce(add, [1, 2, 3, 4])

# def fn(x, y):
#     return x * 10 + y
# reduce(fn, [1, 2, 3, 4])

# def char2num(s):
#     digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#     return digits[s]
# reduce(fn, map(char2num, '1234'))

# DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
# def str2int(s):
#     def fn(x, y):
#         return x * 10 + y
#     def char2num(s):
#         return DIGITS[s]
#     return reduce(fn, map(char2num, s))

# DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
# def char2num(s):
#     return DIGITS[s]
# def str2int(s):
#     return reduce(lambda x, y:  x * 10 + y, map(char2num, s))


#  test

# def normalize(name):
#     return name.title()
# L1 = ['adam', 'LISA', 'barT']
# L2 = list(map(normalize, L1))
# print(L2)

# def ml(x, y):
#     return x * y
# def prod(L):
#     return reduce(ml, L)
# print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
# if prod([3, 5, 7, 9]) == 945:
#     print('测试成功!')
# else:
#     print('测试失败!')

# DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
# def char2nmum(s):
#     return DIGITS[s]
# def str2float(s):
#     parts = s.split('.')
#     integer = reduce(lambda x, y: x * 10 + y, map(char2nmum, parts[0]))
#     decimal = reduce(lambda x, y: x * 10 + y, map(char2nmum, parts[1])) * 10**(-len(parts[1]))
#     return integer + decimal

# print('str2float(\'123.456\') =', str2float('123.456'))
# if abs(str2float('123.456') - 123.456) < 0.00001:
#     print('测试成功!')
# else:
#     print('测试失败!')


#   filter function

# def is_odd(n):
#     return n % 2 == 1
# n1 = list(filter(is_odd, [1, 2, 3, 4, 5, 6]))
# print(n1)

# def not_empty(s):
#     return s and s.strip()
# n2 = list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))
# print(n2)

# def i_odd_iter():
#     n  = 1
#     while True:
#         n = n + 2
#         yield n 
# def _not_divisbile(n):
#     return lambda x: x % n > 0
# def primes():
#     yield 2
#     it = i_odd_iter()
#     while True:
#         n = next(it)
#         yield n
#         it = filter(_not_divisbile(n), it)
# for n in primes():
#     if n < 1000:
#         print(n)
#     else:
#         break

# def is_palindrome(n):
#     return n == int(str(n)[::-1])
# result = filter(is_palindrome, range(1, 200))
# print("result:", list(result))

# output = filter(is_palindrome, range(1, 1000))
# print('1~1000:', list(output))
# if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
#     print('测试成功!')
# else:
#     print('测试失败!')

#  sorted function

# s1 = sorted([36, 5, -12, 9, -21], key = abs)
# print(s1)

# s2 = sorted(['bob', 'about', 'Zoo', 'Credit'], key = str.upper, reverse = True)
# print(s2)

# #test


# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# # def by_name(t):
#     return t[0]
# L2 = sorted(L, key=by_name)
# print(L2)
# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# def by_score(t):
#     return -t[1]
# L2 = sorted(L, key=by_score)
# print(L2)




