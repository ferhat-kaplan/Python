# parent class
class Animal:
    def __init__(self):
        print('animal is created')
        self.osman = 'osman'

    def toString(self):
        print('animal')

    def walk(self):
        print('animal walk')


# child class
class Monkey(Animal):
    def __init__(self):
        super().__init__()  # use init of parent (Animal) class
        print('monkey is created')
        self.cabbar = 'cabbar'

    def toString(self):
        print('monkey')

    def climb(self):
        print('monkey can climb')


class Bird(Animal):
    def __init__(self):
        super().__init__()
        print('bird is crated')

    def fly(self):
        print('flye')


m1 = Monkey()

print(m1.osman)
print(m1.cabbar)


b1 = Bird()
b1.walk()