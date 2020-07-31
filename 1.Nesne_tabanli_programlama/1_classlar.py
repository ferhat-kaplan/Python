# __init__'in içinde self ile tanımlanan herşeye clasın içinden erişebiliriz

class Arabalar():
    def __init__(self, model='boş', renk='boş', beygir_gücü='boş', silindir='boş'):
        self.model = model
        self.renk = renk
        self.beygir_gücü = beygir_gücü
        self.silindir = silindir


# Avantajı dışarıdan her seferinde tek tek değişken oluşturmak yerine
# Hızlı bir şekilde benzer özelliklere sahip değişken classları oluşturabiliriz.

araba1 = Arabalar('Ranault Megane', 'gümüş', 110, 4)
araba2 = Arabalar('Murat 131', 'Kırmızı', 60, 4)
araba3 = Arabalar('Ferrari')


