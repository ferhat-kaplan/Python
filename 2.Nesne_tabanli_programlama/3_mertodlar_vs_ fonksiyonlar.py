class Emp(object):

    age = 25
    salary = 1000

    # Bu bir method dur, methodlar clasın içinde tanımlanır.
    def ageSalaryRatio(self):
        a = self.age / self.salary
        print('Method: ', a)


# Bu bir fonksiyondur.
def ageSalaryRatio(age, salary):
    a = age / salary
    print('fonksiyon :', a)


e1 = Emp()
e1.ageSalaryRatio()

ageSalaryRatio(30, 3000)
