# super Overriding'e uğaramış yani iptal olmuş fonksiyonları tekrar kullanmamızı sağlıyor.
class Çalışan():

    def __init__(self, isim, maaş, departman):
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


class Yonetici(Çalışan):
    def __init__(self, isim, maaş, departman):
        # Yukarıdaki isim  maaş departman değişkenlerini çağırmak için super'i kullandık
        # supere parametre vermezsek yukardaki init fonksiyonunun içindekilerinin hepsini çağırır.
        super().__init__(isim, maaş, departman)
        # Artık yukarıdaki bilgileri_göster fonksiyonunu kullanabiliriz.
        super().bilgileri_göster()


    def bilgileri_göster(self):
        print('Yönetici sınıfı içi')


yonetici1 = Yonetici('osman', 3000, 'çaycı')
yonetici1.bilgileri_göster()
