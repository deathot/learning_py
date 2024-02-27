import types
def fn():
    pass

type(fn) == types.FunctionType
type(abs) == types.BuiltinFunctionType

class animal(object):
    pass
class Dog(animal):
    pass
class Husky(Dog):
    pass
a = animal()
d = Dog()
h = Husky()

isinstance(h, Husky)
isinstance(h, Dog)
isinstance(h, animal)
isinstance(h, animal) and isinstance(h, Dog)
isinstance([1, 2, 3], (list, tuple))

dir('ABC')
len('abc')
'abc'.__len__()

class mydog(object):
    def __len__(self):
        return 6
dog = mydog()
len(dog)

class Myobject(object):
    def __init__(self):
        self.x = 2
    def power(self):
        return self.x *self.x
obj = Myobject()

hasattr(obj, 'x')
obj.x
hasattr(obj, 'u')
setattr(obj, 'u', 10)
hasattr(obj, 'u')
getattr(obj, 'u')
obj.u

getattr(obj, 'z', 404)
fn = getattr(obj, 'power')

def readImage(fp):
    if hasattr(fp, 'read'):
        return readImage(fp)
    return None