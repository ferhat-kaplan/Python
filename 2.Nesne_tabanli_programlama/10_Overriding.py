class Animal: # parent
    def toString(self):
        print('animal')


class Monkey(Animal):

    def toString(self):
        print('monkey')


m1 = Monkey()
m1.toString()  # monkey calls overridinng method
