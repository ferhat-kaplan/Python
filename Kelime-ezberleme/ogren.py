import sqlite3
import time

# sqlite dosyası yoksa oluşturuyoruz,  dosya varsa bağlantı kuruyoruz.
vt = sqlite3.connect('kelimeler.sqlite')
# imleç oluşturuyoruz
im = vt.cursor()

# 'kelime deposu' isimli bir tablo ve 'türkçe, ingilizce' isminde 2 sütun oluşturuyoruz.
im.execute("""CREATE TABLE IF NOT EXISTS 'kelime deposu' (türkçe, ingilizce)""")


def aktarım_görüntüsü():
    for i in range(50):
        time.sleep(0.02)
        print('#', end='')
    print('')


def kelime_ekle():
    while True:
        print("""Kelime eklemede çıkmak için 'q' devam etmek için 'enter'e basınız.""")
        cıkısKontrol = input('')
        if cıkısKontrol == 'q':
            print('\n'*20)
            break
        ing = input('İngilizce kelime : ')
        turk = input('Türkçe karşılığı : ')

        # kelime deposu tablosuna kelimelerimizi ekliyoruz.
        im.execute("""INSERT INTO 'kelime deposu' VALUES (?, ?)""", (turk, ing))
        vt.commit()


def kelime_öğren():
    print('Türkçe kelimelerin karşısına inglizce anlamlarını yazınız.')
    # tablomuzdaki verileri alıyoruz.
    im.execute("""SELECT * FROM 'kelime deposu'""")
    
    for i in im:
        while True:
            for sayac in range(3):
                kelimekontrol = input(i[0] + ' : ')
                if kelimekontrol == i[1]:
                    print('Doğru')
                    break
                else:
                    print('Yanlış')
                if sayac == 2:
                    print(i[0], '=', i[1])
            break
        print('#'*50)
    print('Kelimeler bitti ana seçeneklere yönlendirliyorsunuz')
    aktarım_görüntüsü()


def mainFonk():
    while True:
        print("""
Kelime eklemek için '1'
    
Kelime öğrenmek için '2'
    
Çıkmak için 'q' tuşuna basınız.
        """)
        anaKontrol = input('İşleminizi giriniz : ')

        if anaKontrol == '1':
            aktarım_görüntüsü()
            kelime_ekle()

        elif anaKontrol == '2':
            aktarım_görüntüsü()
            kelime_öğren()

        elif anaKontrol == 'q':
            aktarım_görüntüsü()
            break
        else:
            print('\n'*10, 'Yanlış karakter girdiniz.')
            aktarım_görüntüsü()


mainFonk()
vt.close()
