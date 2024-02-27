from collections.abc import Iterable 
d = {'a' : 1, 'b' : 2, 'c' : 3}
#for key in d:
    #print(key)
#for value in d.values():
    #print(value)
for k, va in d.items():
    print(k, va)
for x in [0, 1, 2, 3, 4]:
    print(x)
for i, val in enumerate (['A', 'B', 'C']):
    print(i, val)

def findMinAndMax(L):
    
    if not L:
        return(None, None)
    else:
        min_val = max_val = L[0]
        for i in L:
            if min_val > i:
                min_val = i
            elif max_val < i:
                max_val = i
    return(min_val, max_val)

if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')

        
        