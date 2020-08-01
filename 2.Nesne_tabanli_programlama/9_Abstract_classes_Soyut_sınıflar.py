from abc import ABC, abstractmethod


# 1.  Soyut sınıflarda hiçbir şekilde a1 = Animal() şeklinde super classı kullanamayız
# Bunu yapabilmek için abc modülünden yararlanıyoruz.
# 2. olarak super classda kulandığım metodları sup classda kullanmak zorundayım.
class Animal(ABC):  # super class

    @abstractmethod
    def walk(self): pass

    @abstractmethod
    def run(self): pass


class Bird(Animal): # sub class

    def __init__(self):
        print('bird')

    def walk(self):
        print('walk')

    def run(self):
        print('run')
