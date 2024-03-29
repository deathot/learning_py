# std1 = {'name': 'daethot', 'score': 100}
# std2 = {'name': 'Bod', 'score': 90}

# def print_score(std):
#     print('%s: %s' % (std['name'], std['score']))
# print_score(std1)

class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))
    
    def get_grade(self):
        if self.score <= 60:
            return 'A'
        elif self.score <= 80:
            return 'B'
        else:
            return 'C'

bart = Student('Bart Simpson', 50)
lisa = Student('Lisa Simpson', 80)
print(bart.print_score(), bart.get_grade())
print(bart.name, bart.get_grade())
