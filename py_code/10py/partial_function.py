def int2(x, base = 2):
    return int(x, base)
s = int2('100000')
import functools
int8 = functools.partial(int, base = 8)
s8 = int8('65565')
print(s8)