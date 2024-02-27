# from enum import Enum

# Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

# for name, member in Month.__members__.items():
#     print(name, '=>', member, ',', member.value)

# from enum import Enum, unique

# @unique
# class Weekday(Enum):
#     Sun = 0
#     Mon = 1
#     Tue = 2
#     Wed = 3
#     Thu = 4
#     Fri = 5
#     Sat = 6
# for name, member in Weekday.__members__.items():
#     print(name, '=>', member, member.value)

from enum import Enum, unique

class Gender(Enum):
    Male = 0
    Female = 1
    
class Student(object):
    def __init__(self, name, gender:Gender):
        self.name = name
        if not isinstance(gender,Gender):
            raise ValueError('must be enumraters')
        self.gender = gender

bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('sussced')
else:
    print('failed')

print(Gender['Male'])

# 下面的代码中，这段是什么意思，def __init__(self, name, gender:Gender):
# class Gender(Enum):
#     Male = 0
#     Female = 1
    
# class Student(object):
#     def __init__(self, name, gender:Gender):
#         self.name = name
#         if not isinstance(gender,Gender):
#             raise ValueError('must be enumraters')
#         self.gender = gender