# def calc_sum(*args):
#     ax = 0
#     for n in args:
#         ax += n
#     return ax

# def lazy_sum(*args):
#     def sum():
#         ax = 0
#         for n in args:
#             ax += n
#         return ax
#     return sum
# f = lazy_sum(1, 3, 4)
# print(f)
# print(f())

# def count():
#     fs = []
#     for i in range(1, 4):
#         def f():
#             return i * i
#         fs.append(f)
#     return fs
# f1, f2, f3 = count()
# print(f1(), f2(), f3())

# def count():
#     def f(i):
#         def g():
#             return i * i
#         return g
#     fs = []
#     for i in range(1, 4):
#         fs.append(f(i))
#     return fs
# f1, f2, f3 = count()
# print(f1(), f2(), f3())


#  test

def createCounter():
    x = 0
    def counter():
        nonlocal x
        x += 1
        return x
    return counter

counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')


    