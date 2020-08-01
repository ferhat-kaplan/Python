class BankAccount(object):

    def __init__(self, name, money, address):
        self.name = name  # Global
        # moneyin başına __ ekleyerek dışarıdan erişimini kapatıyoruz. Bunu methodlarda bile kullanabilirsiniz.
        self.__money = money  # Private
        self.address = address

    # get ve set metodlarını kullanarak dışarıdan erişimi açabiliriz.
    # get and set
    def getMoney(self):
        # __money bilgisini dışarı aktar.
        return self.__money

    def setMoney(self, amount):
        # __money'e ekleme yap
        self.__money += amount


p1 = BankAccount('cabbar', 3000, 'hawai')
p2 = BankAccount('mahmut', 12, 'fakirhane')

# Parayı göster
print(p1.getMoney())
# Parayı arttır
p1.setMoney(20000)
# Parayı göster
print(p1.getMoney())
