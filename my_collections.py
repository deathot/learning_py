#nametuple
from collections import namedtuple

# Point = namedtuple('Point', ['x', 'y'])
# p = Point(1, 2)
# p.x

# Circle = namedtuple('Circle', ['x', 'y', 'r'])

#deque
# from collections import deque

# q = deque(['a', 'b', 'c'])
# q.append('x') #pop()
# q.appendleft('y')
# print(q)

# #defaultdict
# from collections import defaultdict

# dd = defaultdict(lambda: 'N/A')
# dd['key1'] = 'abc'
# print(dd['key2'])

# #OrderedDict
from collections import OrderedDict
# od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
# print(od)

# od = OrderedDict()
# od['z'] = 1
# od['r'] = 3
# od['y'] = 2
# print(list(od.keys()))

# class Lastupdateorderedict(OrderedDict):
    
#     def __init__(self, capacity):
#         super(Lastupdateorderedict, self).__init__()
#         self._capacity = capacity

#     def __setitem__(self, key, value):
#         containsKey = 1 if key in self else 0
#         if len(self) - containsKey >= self._capacity:
#             last = self.popitem(last = False)
#             print('Remove:', last)
#         if containsKey:
#             del self[key]
#             print('set:', (key, value))
#         else:
#             print('add:', (key, value))
#         OrderedDict.__setitem__(self, key, value)
# #define cache capcaity
# cache_capacity = 5
# file_cache = Lastupdateorderedict(cache_capacity)

# def get_file_content(filename):
#     content = f"内容来自文件:{filename}"
#     return content

# def get_cache_file_content(filename):
#     if filename in file_cache:
#         print(f"命中缓存：{filename}")
#         return file_cache[filename]
#     else:
#         print(f"未命中：{filename}")
#         content = get_file_content(filename)
#         file_cache[filename] = content
#         return content

# filename1 = "file1.txt"
# filename2 = "file2.txt"
# filename3 = "file3.txt"
# filename4 = "file4.txt"
# filename5 = "file5.txt"
# filename6 = "file6.txt"

# get_cache_file_content(filename1)
# get_cache_file_content(filename2)
# get_cache_file_content(filename3)
# get_cache_file_content(filename4)
# get_cache_file_content(filename5)
# get_cache_file_content(filename1)
# get_cache_file_content(filename6)

#ChainMap
# from collections import ChainMap
# import os, argparse

# defaults = {
#     'color':'red',
#     'user':'guest'

# }

# parser = argparse.ArgumentParser()
# parser.add_argument('-u', '--user')
# parser.add_argument('-c', '--color')
# namespace = parser.parse_args()
# command_line_args = {k:v for k, v in vars(namespace).items()if v}

# combined = ChainMap(command_line_args, os.environ, defaults)


# print('color = %s' % combined['color'])
# print('user = %s' % combined['user'])

#Counter
from collections import Counter

c = Counter()
for ch in 'deathot':
    c[ch] = c[ch] + 1
c.update('deathot')
print(c)

