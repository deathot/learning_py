# class Student(object):
#     __slots__ = ('name', 'age')

# s = Student()
# s.name = 'deathot'
# print(s.name)

# def set_age(self,age):
#     self.age = age


# Student.set_age = set_age

# from types import MethodType
# s.set_age = MethodType(set_age, s)
# s.set_age(21)
# s.age

# s2 = Student()
# s2.set_age(25)
# s2.age

class Student(object):
    __slots__ = ('name', 'age', 'score')


s = Student()
s.name = 'deathot'
s.age = 21
s.score = 200
s.male('male')

class Bob(Student):
    pass
bob = Bob()
bob.score = 90
