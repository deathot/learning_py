# class Student(object):
#     def get_score(self):
#         return self._score
    
#     def set_score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('mis')
#         if value < 0 or value > 100:
#             raise ValueError('missc')
#         self._score = value
# s = Student()
# s.set_score(99)
# s.get_score()
# s.set_score(9999)

# class Student(object):

#     @property
#     def score(self):
#         return self._score

#     @score.setter
#     def score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer!')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0 ~ 100!')
#         self._score = value

# s = Student()
# s.score = 90
# s.score

# class Student(object):

#     @property
#     def birth(self):
#         return self._birth
    
#     @birth.setter
#     def birth(self, value):
#         self._birth = value
    
#     @property
#     def age(self):
#         return 2024 - self._birth
# dir('Student')

class Screen(object):
    def __init__(self):
        self.height = 0
        self.width = 0
    @property
    def width(self):
        return self._width
    @property
    def height(self):
        return self._height
    
    @width.setter
    def width(self, value):
        self._width = value
    @height.setter
    def height(self, value):
        self._height = value
    
    @property
    def resolution(self):
        return self._width * self._height
s = Screen()
s.width = 1024
s.height = 768
# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')