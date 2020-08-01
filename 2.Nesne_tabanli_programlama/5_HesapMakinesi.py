class Calc(object):
    "calculator"

    # init metodu
    def __init__(self, a, b):
        "initalize values"

        # attribute
        self.value1 = a
        self.value2 = b

    def add(self):
        "addition a+b = result -> return result"
        return self.value1 + self.value2

    def multiply(self):
        "multiplication a*b = result -> return result"
        return self.value1 * self.value2


print('Choose add(1), multiply(2)')
selection = input('select 1 or 2 :')

v1 = int(input('fist value: '))
v2 = int(input('second value: '))

c1 = Calc(v1, v2)

if selection == '1':
    add_result = c1.add()
    print('Add : {}'.format(add_result))
elif selection == '2':
    multiply_result = c1.multiply()
    print('Multiply : {}'.format(multiply_result))
