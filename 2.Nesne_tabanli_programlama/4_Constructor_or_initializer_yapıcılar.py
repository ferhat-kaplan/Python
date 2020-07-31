class Animal(object):

    # Buna constructor yada initializer veya yapıcılar denir.
    def __init__(self, age, name):

        self.name = name
        self.age = age

    def getAge(self):
        return self.age


a1 = Animal(3, 'dog')
a1_age = a1.getAge()
print(a1_age)