from PIL import ImageGrab, ImageOps
import pyautogui
import time
from numpy import *


class Zıpsıp:

    def __init__(self):
        self.yenidenBaslaKordinat = (720, 357)  # Yeniden başla işaretinin kordinatları
        self.dinazorKordinat = (520, 355)    # Dinazorun üst kordinatları
        self.genişlik = 180  # ekran görüntüsünü alacağımız alanın genişliği
        self.yükseklik = 32  # ekran görüntüsünü alacağımız alanın yüksekliği

        a = 0.25  # zaman değişkeni
        sayac = 1  # zıplama sayısını tutan değişken.
        s = self.imageGrab()  # imageGrab() fonksiyonunu değerini s'e atadık.
        self.yenidenBaşlat()  # yeniden başlata tıklar

        while True:
            if self.imageGrab() != s:  # eğer ekrana engel çıkarsa zıpla
                # oyun zamanlar hızlandığı için zıplama bekleme süresi azaltmamız lazım.
                if sayac % 35 == 0:  # 35 kere zıpladığında bekleme süresini azaltır
                    a /= 1.25
                    print(a)
                time.sleep(a)  # a değişkeninin değeri kadar bekler
                print(self.alan)
                sayac += 1
                print(self.mesafe)
                print(sayac)
                self.zipla()
                time.sleep(0.1)

    def yenidenBaşlat(self):  # yeniden başla tuşuna işaretine tıklar.
        pyautogui.click(self.yenidenBaslaKordinat)

    def zipla(self):  # space basarak zıplatır.
        pyautogui.keyDown('space')
        time.sleep(0.05)
        pyautogui.keyUp('space')

    def imageGrab(self):  # Belirlediğimiz alandaki rengi bir sayısal değere dönüştürüyoruz.
        # Taranacak alanı tanımladık. Sol üst x1,y1  sağ alt x2,y2, yani dikdörtgenin sol üst kordinatı ve sağ alt kordinatı
        self.alan = (self.dinazorKordinat[0], self.dinazorKordinat[1], self.dinazorKordinat[0] + self.mesafe, self.dinazorKordinat[1] + self.yükseklik)  # x1,y1  x2,y2
        goruntu = ImageGrab.grab(self.alan)  # belirtiğimiz ekranın anlık görüntüsünü alır
        griGoruntu = ImageOps.grayscale(goruntu)  # Görüntüyü gri tonlamaya dönüştürür.
        s = array(griGoruntu.getcolors())
        return s.sum()


Zıpsıp()
