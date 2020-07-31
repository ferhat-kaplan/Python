class Kitap():

    def __init__(self, isim, yazar, sayfa_sayısı, tür):
        print('init fonksiyonu')
        self.isim = isim
        self.yazar = yazar
        self.sayfa_sayısı = sayfa_sayısı
        self.tür = tür

    def __str__(self):
        return 'İsim: {}\nYazar: {}\nSayfa Sayısı: {}\nTürü: {}\n'.format(self.isim, self.yazar, self.sayfa_sayısı,
                                                                          self.tür)

    def __len__(self):
        return self.sayfa_sayısı

    def __del__(self):
        print('Kitap objesi siliniyor')


kitap = Kitap('İstanbul Hatırası', 'Ahmet Ümit', 561, 'Polisiye')

print(len(kitap))

print(str(kitap))
del kitap

# https://diveintopython3.net/special-method-names.html
