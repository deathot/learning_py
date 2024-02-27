list(range(1, 100))
print(list)

L = []
for x in range(1, 11):
    L.append(x + 1)
print(L)


L= [x * x for x in range(1, 10) if x % 2 != 0]
print(L)
MN = [m + n for m in 'ABC' for n in 'XYZ']
print(MN)

import os
dir = [d for d in os.listdir('.')]
print(dir)

dict = {'0':'A', '1':'B', '2':'C'}
kv = [k + '=' + v for k, v in dict.items()]
print(kv)
for k, v in dict.items():
    print(k, '=', v)

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]
print(L2)
