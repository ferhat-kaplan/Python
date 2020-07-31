# miras alma

class Çalışan():

    def __init__(self, isim='...', maaş='...', departman='...'):
        print('çalışan sınıfının init fonksiyonu')

        self.isim = isim
        self. maaş = maaş
        self.departman = departman

    def bilgileri_göster(self):
        print('Çalışan sınıf bilgileri')

        print('İsim : {} \nMaaş : {} \nDepartman : {}\n'.format(self.isim, self.maaş, self.departman))

    def departman_değiş(self, yeni_departman):
        print('Departman değiştiriliyor.')

        self.departman = yeni_departman


# Yonetici sınıfı Çalışan sınıfını  miras aldı.
# Böylelikle aynı özelikleri baştan yazmak yerine Çalışan sınıfından kendini aktardı.
# Ortak özellikleri bir sınıfa yazarak ondan miras alabilir ve tekrar ortak ozellikleri ayrı  ayrı yazmak zorunda kalmazsınız
class Yonetici(Çalışan):
    # init fonksiyonunu tekrar tanımladığımız için yukarıdakini iptal oldu
    # Yani isim maaş deparman değişkenlerini artık kullanamayız.
    def __init__(self, isim='cabbar'):

        self.isim = isim

        # Overriding (İptal etme)
        # Eğer sınıfın içinde, miras aldığımız sınıfın içindeki aynı isimde fonksiyon yada değişken var ise
        # Önceliği bulunduğu sınıfa verir ve miras alınan sınıftakini görmezden gelir.

    def bilgileri_göster(self):
        print('Yönetici sınıfı içi')


yonetici1 = Yonetici()

