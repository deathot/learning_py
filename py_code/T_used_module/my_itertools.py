from itertools import cycle, islice, count
import itertools
def pi(N):
    ' 计算pi的值 '
    natuals = itertools.count(1)
    ns = itertools.takewhile(lambda x: x <= 2*N - 1 , natuals)
    oddL = [x for x in ns if x % 2 != 0]
    signs = cycle([4, -4])
    ser = (next(signs) / odd for odd in oddL)
    return sum(ser)

# 测试:
print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')
