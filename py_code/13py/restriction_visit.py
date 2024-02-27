class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name
    
    def get_score(self):
        return self.__score
    
    def set_score(self, score):
        if 0 <= score <= 100:  
            self.__score = score
        else:
            raise ValueError('bad score')

bart = Student('Bart Sim', 80)
print(bart.get_name())
bart.set_score(90)
print(bart.get_score())

# class Student(object):
#     def __init__(self, name, score):
#         self.__name = name
#         self.__score = score

#     def get_name(self):
#         return self.__name
#     def get_score(self):
#         return self.__score
#     def set_score(self, score):
#         if 0 <= score <= 100:  
#             self.__score = score
#         else:
#             raise ValueError('bad score')

# bart = Student('Bart Sim', 80)
# print(bart.get_name())
# bart.set_score(90)
# print(bart.get_score())

# class Student(object):
#     def __init__(self, name, gender):
#         self.name = name
#         self.__gender = gender

#     def get_gender(self):
#         return self.__gender
    
#     def set_gender(self, gender):
#         if gender == 'male':
#             self.__gender = gender
#         elif gender == 'female':
#             self.__gender  = gender
#         else:
#             raise ValueError('invalid input')

# # 测试:
# bart = Student('Bart', 'male')
# if bart.get_gender() != 'male':
#     print('测试失败!')
# else:
#     bart.set_gender('female')
#     if bart.get_gender() != 'female':
#         print('测试失败!')
#     else:
#         print('测试成功!')


