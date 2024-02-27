import pickle
import json

# d = dict(name = 'deathot', age = 21, score = 100)
# #print(pickle.dumps(d))

# f = open('dump.txt', 'wb')
# pickle.dump(d, f)
# f.close()
# f = open('dump.txt', 'rb')
# d = pickle.load(f)

# print(json.dumps(d))

# json_str = '{"name": "deathot", "age": 21, "score": 100}'
# print(json.loads(json_str))

# def student2dict(std):
#     return {
#         'name': std.name,
#         'age': std.age,
#         'score': std.score
#     }

# class Student(object):
#     def __init__(self, name, age, score):
#         self.name = name
#         self.age = age
#         self.score = score

# s = Student('deathot', 21, 100)
# print(json.dumps(s, default = lambda obj: obj.__dict__))

# def dict2student(d):
#     return Student(d['name'], d['age'], d['score'])

# json_str = '{"name": "deathot", "age": 21, "score": 100}'
# print(json.loads(json_str, object_hook = dict2student))

