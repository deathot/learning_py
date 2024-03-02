#nametuple
from collections import namedtuple

# Point = namedtuple('Point', ['x', 'y'])
# p = Point(1, 2)
# p.x

# Circle = namedtuple('Circle', ['x', 'y', 'r'])

#deque
from collections import deque

q = deque(['a', 'b', 'c'])
q.append('x') #pop()
q.appendleft('y')
print(q)

#defaultdict
from collections import defaultdict

dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key2'])