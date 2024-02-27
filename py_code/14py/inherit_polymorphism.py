class Animal(object):
    def run(self):
        print('Animal is running')

class Dog(Animal):
    def run(self):
        print('Dog is running')
class Cat(Animal):
    def run(self):
        print('Cat is fall sleep')

# dog = Dog()
# dog.run()
# cat = Cat()
# cat.run()

# c = Dog()
# b = Animal()
# isinstance(c, Animal)

def run_twice(animal):
    animal.run()
    animal.run()

class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly')

run_twice(Tortoise())

class Timer(object):
    def run(self):
        print('start')

time = Timer()
time.run()
    


