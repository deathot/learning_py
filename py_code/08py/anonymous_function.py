L1 = list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(L1)

f = lambda x: x * x
print(f(3))

def build(x, y):
    return lambda x, y: x + y

#  test

L = list(filter(lambda n: n % 2 == 1, range(1, 20)))
print(L)
