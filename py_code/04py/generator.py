g = (x*x for x in range(10))
for i in g:
    print(i)

def fib(max):
    n ,a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1
    return'done'
for i in fib(6):
    print(i)
g = fib(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break

def odd():
    print('step1')
    yield (1)
    print('step2')
    yield (2)
    print('step3')
    yield (3)

g = odd()
for i in g:
    print(g)

def triangles():        #n=1 k=1 L[0] + L[1] n=2 k=1,2 
    L = [1]
    n = 0
    results = []
    while True:
        results = [1] 
        yield L
        for k in range(1, n+1):
            results.append(L[k-1] + L[k])
        results.append(1)
        n += 1
        L = results
n = 0
results = []
for t in triangles():
    results.append(t)
    n = n + 1
    if n == 10:
        break

for t in results:
    print(t)

if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')
        
    