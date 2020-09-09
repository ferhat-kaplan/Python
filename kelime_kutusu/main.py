import sys, os, sqlite3
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtCore import *
from threading import Thread
import requests
from bs4 import BeautifulSoup
import re
import playsound
from googletrans import Translator
import tkinter as tk
from time import sleep
from os import system
from os import name
if name == 'nt':
    from win10toast import ToastNotifier
    toaster = ToastNotifier()


class KutuUc(object):
    def setupUi(self, AnaPencere):
        AnaPencere.setWindowTitle('Kelime Kutusu')
        AnaPencere.setGeometry(600, 150, 500, 500)
        AnaPencere.setFixedSize(500, 500)
        self.centralwidget = QWidget(AnaPencere)
        AnaPencere.setCentralWidget(self.centralwidget)
        ###############################################
        AnaPencere.arkaplan = QLabel(self.centralwidget)
        AnaPencere.arkaplan.setPixmap(QPixmap('kutu1Arkaplan.png'))
        #############################################################
        self.cevap = QLineEdit(self.centralwidget)
        self.cevap.move(181, 152)
        self.cevap.returnPressed.connect(self.sonraki)
        #######################################################################
        AnaPencere.kutuikiyazısı = QLabel(self.centralwidget)
        AnaPencere.kutuikiyazısı.setPixmap(QPixmap('KUTU3Yazısı.png'))
        AnaPencere.kutuikiyazısı.move(198, 10)
        #######################################################################
        AnaPencere.cevapButon = QPushButton('Cevap', self.centralwidget)
        AnaPencere.cevapButon.move(364, 144)
        AnaPencere.cevapButon.resize(116, 28)
        AnaPencere.cevapButon.setStyleSheet('background-color:#058F3C;color: white;')
        AnaPencere.cevapButon.setFont(QFont('Arial', 16, weight=QFont.Bold))
        ###########################################################################
        self.gecButon = QPushButton('Geç', self.centralwidget)
        self.gecButon.move(1000, 1000)
        self.gecButon.resize(116, 28)
        self.gecButon.setStyleSheet('background-color:#058F3C;color: white;')
        self.gecButon.setFont(QFont('Arial', 16, weight=QFont.Bold))
        ###########################################################################
        self.geriButon = QPushButton('Geri', self.centralwidget)
        self.geriButon.setStyleSheet('background-color:#FFD600;')
        self.geriButon.move(160, 400)
        self.geriButon.resize(184, 34)
        self.geriButon.setFont(QFont('Arial', 16, weight=QFont.Bold))
        self.geriButon.setAutoDefault(True)
        ###########################################################################
        self.kelime = QLabel('', self.centralwidget)
        self.kelime.move(181, 120)
        self.kelime.setFont(QFont('Arial', 13, weight=QFont.Bold))
        self.kelime.setTextInteractionFlags(Qt.TextSelectableByMouse)
        ###########################################################################
        self.dinle = QPushButton('Dinle', self.centralwidget)
        try:
            self.dinle.clicked.connect(self.chek)
        except:
            pass
        self.dinle.move(194, 194)
        self.dinle.resize(116, 28)
        self.dinle.setStyleSheet('background-color:#058F3C;color: white;')
        self.dinle.setFont(QFont('Arial', 16, weight=QFont.Bold))
        ############################################################################
        self.yanlısCevapYazısı = QLabel('', self.centralwidget)
        self.yanlısCevapYazısı.move(181, 30)
        self.yanlısCevapYazısı.setFont(QFont('Arial', 22, weight=QFont.Bold))

        self.dogruCevap = QLabel('', self.centralwidget)
        self.dogruCevap.move(181, 100)

        ############################################################################
        vt = sqlite3.connect('kelimeler.db')
        im = vt.cursor()
        im.execute('CREATE TABLE IF NOT EXISTS kutubir (turkce TEXT, ingilizce TEXT, deger INT)')
        im.execute('CREATE TABLE IF NOT EXISTS kutuiki (turkce TEXT, ingilizce TEXT, deger INT)')
        im.execute('CREATE TABLE IF NOT EXISTS kutuuc (turkce TEXT, ingilizce TEXT, deger INT)')
        im.execute('SELECT * FROM kutuuc')
        self.data = im.fetchall()
        ##################################################################
        self.tekrarla = QPushButton('Yeniden Başla', self.centralwidget)
        self.tekrarla.move(1000, 1000)
        ###################################################################
        self.sill = QPushButton('Sil', self.centralwidget)
        self.sill.clicked.connect(self.silfunc)
        self.sill.move(364, 194)
        self.sill.resize(116, 28)
        self.sill.setStyleSheet('background-color:#058F3C;color: white;')
        self.sill.setFont(QFont('Arial', 16, weight=QFont.Bold))
        ###################################################################
        if len(self.data) > 0:
            self.kelime.setText(self.data[0][0])

        AnaPencere.cevapButon.clicked.connect(self.sonraki)
        self.gecButon.clicked.connect(self.gecButonfunc)
        self.kontrol = True
        self.sayac = 0

    def silfunc(self):
        try:
            vt = sqlite3.connect('kelimeler.db')
            im = vt.cursor()
            im.execute('DELETE FROM kutuuc where ingilizce = ?', (self.data[self.sayac][1], ))
            vt.commit()
            vt.close()
            self.sayac += 1
            self.sonrakiKelimeYaz()
        except:
            self.kelime.setText('')

    def chek(self):
        link = 'https://dictionary.cambridge.org/dictionary/english/' + self.data[self.sayac][1] + '?q=' + self.data[self.sayac][1] + 's'
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"}

        r = requests.get(link, headers=header)

        source = BeautifulSoup(r.content, 'lxml')

        data = source.find_all('source', {'type': 'audio/mpeg'})
        liste = []
        for i in data:
            ss = re.search('<source src="(/media/english/us_pron.*)" type="audio/mpeg"/>', str(i))
            try:
                liste.append(ss.group(1))
                # print(ss.group(1))
            except:
                pass

        playsound.playsound("https://dictionary.cambridge.org/" + liste[0],True)

    def sonraki(self):
        if self.kontrol and len(self.data) > 0 and self.cevap.text() == self.data[self.sayac][1]:
            self.yanlısCevapYazısı.setText('')
            self.dogruCevap.setText('')
            self.degerKontrol()
            self.degerArtır()
            self.sayac += 1
            if len(self.data) == self.sayac:
                self.yanlısCevapYazısı.resize(400, 40)
                self.yanlısCevapYazısı.setText('Bitti')

                self.tekrarla.move(364, 114)
                self.tekrarla.resize(116, 28)
                self.tekrarla.setStyleSheet('background-color:#058F3C;color: white;')
                self.tekrarla.setFont(QFont('Arial', 11, weight=QFont.Bold))
                self.tekrarla.setAutoDefault(False)
                self.kontrol = False
                return None
            self.sonrakiKelimeYaz()
        elif self.kontrol and len(self.data) > 0 and self.kelime.text() != self.data[self.sayac][1]:
            self.yanlısCevapYazısı.resize(400, 40)
            self.yanlısCevapYazısı.setText('Yanlış cevap')
            self.dogruCevap.resize(400, 20)
            self.dogruCevap.setText('Doğru cevap : ' + self.data[self.sayac][1])
            self.degerAzalt()
            self.gec()

    def gec(self):
        self.gecButon.move(364, 144)

    def gecButonfunc(self):
        self.degerKontrol()
        self.yanlısCevapYazısı.setText('')
        self.dogruCevap.setText('')
        self.gecButon.move(1000, 1000)
        self.sayac += 1
        if len(self.data) == self.sayac:
            self.yanlısCevapYazısı.resize(400, 40)
            self.yanlısCevapYazısı.setText('Bitti')

            self.tekrarla.move(364, 114)
            self.tekrarla.resize(116, 28)
            self.tekrarla.setStyleSheet('background-color:#058F3C;color: white;')
            self.tekrarla.setFont(QFont('Arial', 11, weight=QFont.Bold))
            self.tekrarla.setAutoDefault(False)
            self.kontrol = False
            return None
        self.sonrakiKelimeYaz()

    def sonrakiKelimeYaz(self):
        try:
            self.kelime.resize(400, 30)
            self.kelime.setText(self.data[self.sayac][0])
            self.cevap.clear()
        except:
            pass

    def degerArtır(self):
        vt = sqlite3.connect('kelimeler.db')
        im = vt.cursor()

        im.execute('UPDATE kutuuc set deger = ? where ingilizce = ?', (self.data[self.sayac][2] + 1, self.data[self.sayac][1]))
        vt.commit()
        vt.close()

    def degerAzalt(self):
        vt = sqlite3.connect('kelimeler.db')
        im = vt.cursor()

        im.execute('UPDATE kutuuc set deger = ? where ingilizce = ?', (self.data[self.sayac][2] + -1, self.data[self.sayac][1]))
        vt.commit()
        vt.close()

    def degerKontrol(self):
        if self.data[self.sayac][2] >= 9:
            pass
        elif self.data[self.sayac][2] < 0:
            vt = sqlite3.connect('kelimeler.db')
            im = vt.cursor()

            im.execute('UPDATE kutuuc set deger = ? where ingilizce = ?', (0, self.data[self.sayac][1]))
            im.execute('SELECT * FROM kutuuc where ingilizce = ?', (self.data[self.sayac][1],))
            data = im.fetchall()
            im.execute('DELETE FROM kutuuc where ingilizce = ?', (data[0][1],))
            im.execute('INSERT INTO kutuiki VALUES(?, ?, ?)', data[0])
            vt.commit()
            vt.close()


class KutuIki(object):
    def setupUi(self, AnaPencere):
        AnaPencere.setWindowTitle('Kelime Kutusu')
        AnaPencere.setGeometry(600, 150, 500, 500)
        AnaPencere.setFixedSize(500, 500)
        self.centralwidget = QWidget(AnaPencere)
        AnaPencere.setCentralWidget(self.centralwidget)
        ###############################################
        AnaPencere.arkaplan = QLabel(self.centralwidget)
        AnaPencere.arkaplan.setPixmap(QPixmap('kutu1Arkaplan.png'))
        #############################################################
        self.cevap = QLineEdit(self.centralwidget)
        self.cevap.move(181, 152)
        self.cevap.returnPressed.connect(self.sonraki)
        #######################################################################
        AnaPencere.kutuikiyazısı = QLabel(self.centralwidget)
        AnaPencere.kutuikiyazısı.setPixmap(QPixmap('KUTU-2yazısı.png'))
        AnaPencere.kutuikiyazısı.move(198, 10)
        #######################################################################
        AnaPencere.cevapButon = QPushButton('Cevap', self.centralwidget)
        AnaPencere.cevapButon.move(364, 144)
        AnaPencere.cevapButon.resize(116, 28)
        AnaPencere.cevapButon.setStyleSheet('background-color:#058F3C;color: white;')
        AnaPencere.cevapButon.setFont(QFont('Arial', 16, weight=QFont.Bold))
        ###########################################################################
        self.gecButon = QPushButton('Geç', self.centralwidget)
        self.gecButon.move(1000, 1000)
        self.gecButon.resize(116, 28)
        self.gecButon.setStyleSheet('background-color:#058F3C;color: white;')
        self.gecButon.setFont(QFont('Arial', 16, weight=QFont.Bold))
        ###########################################################################
        self.geriButon = QPushButton('Geri', self.centralwidget)
        self.geriButon.setStyleSheet('background-color:#FFD600;')
        self.geriButon.move(160, 400)
        self.geriButon.resize(184, 34)
        self.geriButon.setFont(QFont('Arial', 16, weight=QFont.Bold))
        self.geriButon.setAutoDefault(True)
        ###########################################################################
        self.kelime = QLabel('', self.centralwidget)
        self.kelime.move(181, 120)
        self.kelime.setFont(QFont('Arial', 13, weight=QFont.Bold))
        self.kelime.setTextInteractionFlags(Qt.TextSelectableByMouse)
        ###########################################################################
        self.dinle = QPushButton('Dinle', self.centralwidget)
        try:
            self.dinle.clicked.connect(self.chek)
        except:
            pass
        self.dinle.move(194, 194)
        self.dinle.resize(116, 28)
        self.dinle.setStyleSheet('background-color:#058F3C;color: white;')
        self.dinle.setFont(QFont('Arial', 16, weight=QFont.Bold))
        ############################################################################
        self.yanlısCevapYazısı = QLabel('', self.centralwidget)
        self.yanlısCevapYazısı.move(181, 30)
        self.yanlısCevapYazısı.setFont(QFont('Arial', 22, weight=QFont.Bold))

        self.dogruCevap = QLabel('', self.centralwidget)
        self.dogruCevap.move(181, 100)

        ############################################################################
        vt = sqlite3.connect('kelimeler.db')
        im = vt.cursor()
        im.execute('CREATE TABLE IF NOT EXISTS kutubir (turkce TEXT, ingilizce TEXT, deger INT)')
        im.execute('CREATE TABLE IF NOT EXISTS kutuiki (turkce TEXT, ingilizce TEXT, deger INT)')
        im.execute('CREATE TABLE IF NOT EXISTS kutuuc (turkce TEXT, ingilizce TEXT, deger INT)')
        im.execute('SELECT * FROM kutuiki')
        self.data = im.fetchall()
        ##################################################################
        self.tekrarla = QPushButton('Yeniden Başla', self.centralwidget)
        self.tekrarla.move(1000, 1000)
        ###################################################################
        self.sill = QPushButton('Sil', self.centralwidget)
        self.sill.clicked.connect(self.silfunc)
        self.sill.move(364, 194)
        self.sill.resize(116, 28)
        self.sill.setStyleSheet('background-color:#058F3C;color: white;')
        self.sill.setFont(QFont('Arial', 16, weight=QFont.Bold))
        ###################################################################
        if len(self.data) > 0:
            self.kelime.setText(self.data[0][0])

        AnaPencere.cevapButon.clicked.connect(self.sonraki)
        self.gecButon.clicked.connect(self.gecButonfunc)
        self.kontrol = True
        self.sayac = 0

    def silfunc(self):
        try:
            vt = sqlite3.connect('kelimeler.db')
            im = vt.cursor()
            im.execute('DELETE FROM kutuuc where ingilizce = ?', (self.data[self.sayac][1], ))
            vt.commit()
            vt.close()
            self.sayac += 1
            self.sonrakiKelimeYaz()
        except:
            self.kelime.setText('')

    def chek(self):
        link = 'https://dictionary.cambridge.org/dictionary/english/' + self.data[self.sayac][1] + '?q=' + self.data[self.sayac][1] + 's'
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"}

        r = requests.get(link, headers=header)

        source = BeautifulSoup(r.content, 'lxml')

        data = source.find_all('source', {'type': 'audio/mpeg'})
        liste = []
        for i in data:
            ss = re.search('<source src="(/media/english/us_pron.*)" type="audio/mpeg"/>', str(i))
            try:
                liste.append(ss.group(1))
                # print(ss.group(1))
            except:
                pass

        playsound.playsound("https://dictionary.cambridge.org/" + liste[0],True)

    def sonraki(self):
        if self.kontrol and len(self.data) > 0 and self.cevap.text() == self.data[self.sayac][1]:
            self.yanlısCevapYazısı.setText('')
            self.dogruCevap.setText('')
            self.degerKontrol()
            self.degerArtır()
            self.sayac += 1
            if len(self.data) == self.sayac:
                self.yanlısCevapYazısı.resize(400, 40)
                self.yanlısCevapYazısı.setText('Bitti')

                self.tekrarla.move(364, 114)
                self.tekrarla.resize(116, 28)
                self.tekrarla.setStyleSheet('background-color:#058F3C;color: white;')
                self.tekrarla.setFont(QFont('Arial', 11, weight=QFont.Bold))
                self.tekrarla.setAutoDefault(False)
                self.kontrol = False
                return None
            self.sonrakiKelimeYaz()
        elif self.kontrol and len(self.data) > 0 and self.kelime.text() != self.data[self.sayac][1]:
            self.yanlısCevapYazısı.resize(400, 40)
            self.yanlısCevapYazısı.setText('Yanlış cevap')
            self.dogruCevap.resize(400, 20)
            self.dogruCevap.setText('Doğru cevap : ' + self.data[self.sayac][1])
            self.degerAzalt()
            self.gec()

    def gec(self):
        self.gecButon.move(364, 144)

    def gecButonfunc(self):
        self.degerKontrol()
        self.yanlısCevapYazısı.setText('')
        self.dogruCevap.setText('')
        self.gecButon.move(1000, 1000)
        self.sayac += 1
        if len(self.data) == self.sayac:
            self.yanlısCevapYazısı.resize(400, 40)
            self.yanlısCevapYazısı.setText('Bitti')

            self.tekrarla.move(364, 114)
            self.tekrarla.resize(116, 28)
            self.tekrarla.setStyleSheet('background-color:#058F3C;color: white;')
            self.tekrarla.setFont(QFont('Arial', 11, weight=QFont.Bold))
            self.tekrarla.setAutoDefault(False)
            self.kontrol = False
            return None
        self.sonrakiKelimeYaz()

    def sonrakiKelimeYaz(self):
        try:
            self.kelime.resize(400, 30)
            self.kelime.setText(self.data[self.sayac][0])
            self.cevap.clear()
        except:
            pass

    def degerArtır(self):
        vt = sqlite3.connect('kelimeler.db')
        im = vt.cursor()

        im.execute('UPDATE kutuiki set deger = ? where ingilizce = ?', (self.data[self.sayac][2] + 1, self.data[self.sayac][1]))
        vt.commit()
        vt.close()

    def degerAzalt(self):
        vt = sqlite3.connect('kelimeler.db')
        im = vt.cursor()

        im.execute('UPDATE kutuiki set deger = ? where ingilizce = ?', (self.data[self.sayac][2] + -1, self.data[self.sayac][1]))
        vt.commit()
        vt.close()

    def degerKontrol(self):
        if self.data[self.sayac][2] >= 9:
            vt = sqlite3.connect('kelimeler.db')
            im = vt.cursor()

            im.execute('UPDATE kutuiki set deger = ? where ingilizce = ?', (0, self.data[self.sayac][1]))
            im.execute('SELECT * FROM kutuiki where ingilizce = ?', (self.data[self.sayac][1],))
            data = im.fetchall()
            im.execute('DELETE FROM kutuiki where ingilizce = ?', (data[0][1],))
            im.execute('INSERT INTO kutuuc VALUES(?, ?, ?)', data[0])
            vt.commit()
            vt.close()
        elif self.data[self.sayac][2] < 0:
            vt = sqlite3.connect('kelimeler.db')
            im = vt.cursor()

            im.execute('UPDATE kutuiki set deger = ? where ingilizce = ?', (0, self.data[self.sayac][1]))
            im.execute('SELECT * FROM kutuiki where ingilizce = ?', (self.data[self.sayac][1],))
            data = im.fetchall()
            im.execute('DELETE FROM kutuiki where ingilizce = ?', (data[0][1],))
            im.execute('INSERT INTO kutubir VALUES(?, ?, ?)', data[0])
            vt.commit()
            vt.close()


class KutuBir(object):
    def setupUi(self, AnaPencere):
        AnaPencere.setWindowTitle('Kelime Kutusu')
        AnaPencere.setGeometry(600, 150, 500, 500)
        AnaPencere.setFixedSize(500, 500)
        self.centralwidget = QWidget(AnaPencere)
        AnaPencere.setCentralWidget(self.centralwidget)
        ###############################################
        AnaPencere.arkaplan = QLabel(self.centralwidget)
        AnaPencere.arkaplan.setPixmap(QPixmap('kutu1Arkaplan.png'))
        #############################################################
        AnaPencere.kutubiryazısı = QLabel(self.centralwidget)
        AnaPencere.kutubiryazısı.setPixmap(QPixmap('KUTU1-YAZISI.png'))
        AnaPencere.kutubiryazısı.move(198, 10)
        #############################################################
        self.cevap = QLineEdit(self.centralwidget)
        self.cevap.move(181, 152)
        self.cevap.returnPressed.connect(self.sonraki)
        #######################################################################
        AnaPencere.cevapButon = QPushButton('Cevap', self.centralwidget)
        AnaPencere.cevapButon.move(364, 144)
        AnaPencere.cevapButon.resize(116, 28)
        AnaPencere.cevapButon.setStyleSheet('background-color:#058F3C;color: white;')
        AnaPencere.cevapButon.setFont(QFont('Arial', 16, weight=QFont.Bold))
        ###########################################################################
        self.gecButon = QPushButton('Geç', self.centralwidget)
        self.gecButon.move(1000, 1000)
        self.gecButon.resize(116, 28)
        self.gecButon.setStyleSheet('background-color:#058F3C;color: white;')
        self.gecButon.setFont(QFont('Arial', 16, weight=QFont.Bold))
        ###########################################################################
        self.geriButon = QPushButton('Geri', self.centralwidget)
        self.geriButon.setStyleSheet('background-color:#FFD600;')
        self.geriButon.move(160, 400)
        self.geriButon.resize(184, 34)
        self.geriButon.setFont(QFont('Arial', 16, weight=QFont.Bold))
        self.geriButon.setAutoDefault(True)
        ###########################################################################
        self.kelime = QLabel('', self.centralwidget)
        self.kelime.move(181, 120)
        self.kelime.setFont(QFont('Arial', 13, weight=QFont.Bold))
        self.kelime.setTextInteractionFlags(Qt.TextSelectableByMouse)
        ###########################################################################
        self.yanlısCevapYazısı = QLabel('', self.centralwidget)
        self.yanlısCevapYazısı.move(181, 30)
        self.yanlısCevapYazısı.setFont(QFont('Arial', 22, weight=QFont.Bold))

        self.dogruCevap = QLabel('', self.centralwidget)
        self.dogruCevap.move(181, 100)

        ############################################################################
        self.dinle = QPushButton('Dinle', self.centralwidget)
        try:
            self.dinle.clicked.connect(self.chek)
        except:
            pass
        self.dinle.move(194, 194)
        self.dinle.resize(116, 28)
        self.dinle.setStyleSheet('background-color:#058F3C;color: white;')
        self.dinle.setFont(QFont('Arial', 16, weight=QFont.Bold))
        ############################################################################
        vt = sqlite3.connect('kelimeler.db')
        im = vt.cursor()
        im.execute('CREATE TABLE IF NOT EXISTS kutubir (turkce TEXT, ingilizce TEXT, deger INT)')
        im.execute('CREATE TABLE IF NOT EXISTS kutuiki (turkce TEXT, ingilizce TEXT, deger INT)')
        im.execute('CREATE TABLE IF NOT EXISTS kutuuc (turkce TEXT, ingilizce TEXT, deger INT)')
        im.execute('SELECT * FROM kutubir')
        self.data = im.fetchall()
        vt.commit()
        vt.close()
        ##################################################################
        self.tekrarla = QPushButton('Yeniden Başla', self.centralwidget)
        self.tekrarla.move(1000, 1000)
        ###################################################################
        self.sill = QPushButton('Sil', self.centralwidget)
        self.sill.clicked.connect(self.silfunc)
        self.sill.move(364, 194)
        self.sill.resize(116, 28)
        self.sill.setStyleSheet('background-color:#058F3C;color: white;')
        self.sill.setFont(QFont('Arial', 16, weight=QFont.Bold))

        ###################################################################
        if len(self.data) > 0:
            self.kelime.setText(self.data[0][0])

        AnaPencere.cevapButon.clicked.connect(self.sonraki)
        self.gecButon.clicked.connect(self.gecButonfunc)
        self.kontrol = True
        self.sayac = 0

    def chek(self):
        link = 'https://dictionary.cambridge.org/dictionary/english/' + self.data[self.sayac][1] + '?q=' + self.data[self.sayac][1] + 's'
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"}

        r = requests.get(link, headers=header)

        source = BeautifulSoup(r.content, 'lxml')

        data = source.find_all('source', {'type': 'audio/mpeg'})
        liste = []
        for i in data:
            ss = re.search('<source src="(/media/english/us_pron.*)" type="audio/mpeg"/>', str(i))
            try:
                liste.append(ss.group(1))
                # print(ss.group(1))
            except:
                pass

        playsound.playsound("https://dictionary.cambridge.org/" + liste[0],True)

    def silfunc(self):
        try:
            vt = sqlite3.connect('kelimeler.db')
            im = vt.cursor()
            im.execute('DELETE FROM kutubir where ingilizce = ?', (self.data[self.sayac][1], ))
            vt.commit()
            vt.close()
            self.sayac += 1
            self.sonrakiKelimeYaz()
        except:
            self.kelime.setText('')

    def sonraki(self):
        if self.kontrol and len(self.data) > 0 and self.cevap.text() == self.data[self.sayac][1]:
            self.yanlısCevapYazısı.setText('')
            self.dogruCevap.setText('')
            self.degerKontrol()
            self.degerArtır()
            self.sayac += 1
            if len(self.data) == self.sayac:
                self.yanlısCevapYazısı.resize(400, 40)
                self.yanlısCevapYazısı.setText('Bitti')

                self.tekrarla.move(364, 114)
                self.tekrarla.resize(116, 28)
                self.tekrarla.setStyleSheet('background-color:#058F3C;color: white;')
                self.tekrarla.setFont(QFont('Arial', 11, weight=QFont.Bold))
                self.tekrarla.setAutoDefault(False)
                self.kontrol = False
                return None
            self.sonrakiKelimeYaz()
        elif self.kontrol and len(self.data) > 0 and self.kelime.text() != self.data[self.sayac][1]:
            self.yanlısCevapYazısı.resize(400, 40)
            self.yanlısCevapYazısı.setText('Yanlış cevap')
            self.dogruCevap.resize(400, 20)
            self.dogruCevap.setText('Doğru cevap : ' + self.data[self.sayac][1])
            self.degerAzalt()
            self.gec()

    def gec(self):
        self.gecButon.move(364, 144)

    def gecButonfunc(self):
        self.yanlısCevapYazısı.setText('')
        self.dogruCevap.setText('')
        self.gecButon.move(1000, 1000)
        self.sayac += 1
        if len(self.data) == self.sayac:
            self.yanlısCevapYazısı.resize(400, 40)
            self.yanlısCevapYazısı.setText('Bitti')

            self.tekrarla.move(364, 114)
            self.tekrarla.resize(116, 28)
            self.tekrarla.setStyleSheet('background-color:#058F3C;color: white;')
            self.tekrarla.setFont(QFont('Arial', 11, weight=QFont.Bold))
            self.tekrarla.setAutoDefault(False)
            self.kontrol = False
            return None
        self.sonrakiKelimeYaz()
        self.degerKontrol()

    def sonrakiKelimeYaz(self):
        try:
            self.kelime.resize(400, 30)
            self.kelime.setText(self.data[self.sayac][0])
            self.cevap.clear()
        except:
            pass

    def degerArtır(self):
        vt = sqlite3.connect('kelimeler.db')
        im = vt.cursor()

        im.execute('UPDATE kutubir set deger = ? where ingilizce = ?', (self.data[self.sayac][2] + 1, self.data[self.sayac][1]))
        vt.commit()
        vt.close()

    def degerAzalt(self):
        vt = sqlite3.connect('kelimeler.db')
        im = vt.cursor()

        im.execute('UPDATE kutubir set deger = ? where ingilizce = ?', (self.data[self.sayac][2] + -1, self.data[self.sayac][1]))
        vt.commit()
        vt.close()

    def degerKontrol(self):
        if self.data[self.sayac][2] >= 9:
            vt = sqlite3.connect('kelimeler.db')
            im = vt.cursor()

            im.execute('UPDATE kutubir set deger = ? where ingilizce = ?', (0, self.data[self.sayac][1]))
            im.execute('SELECT * FROM kutubir where ingilizce = ?', (self.data[self.sayac][1],))
            data = im.fetchall()
            im.execute('DELETE FROM kutubir where ingilizce = ?', (data[0][1],))
            im.execute('INSERT INTO kutuiki VALUES(?, ?, ?)', data[0])
            vt.commit()
            vt.close()


class Giris(object):
    def setupUi(self, AnaPencere):
        AnaPencere.setWindowTitle('Kelime Kutusu')
        AnaPencere.setGeometry(600, 150, 500, 500)
        AnaPencere.setFixedSize(500, 500)
        self.centralwidget = QWidget(AnaPencere)
        AnaPencere.arkaplan = QLabel(self.centralwidget)
        AnaPencere.arkaplan.setPixmap(QPixmap('arkaplan.png'))
        AnaPencere.arkaplan.resize(500, 500)
        ####################################################
        AnaPencere.kelimeKutusu = QLabel(self.centralwidget)
        AnaPencere.kelimeKutusu.setPixmap(QPixmap('kelimeKutusu.png'))
        AnaPencere.kelimeKutusu.mousePressEvent = self.link
        AnaPencere.kelimeKutusu.move(130, 10)
        ####################################################
        self.kelimeEkleButonu = QPushButton('Kelime Ekle', self.centralwidget)
        self.kelimeEkleButonu.setStyleSheet('background-color:#FFD600;')
        self.kelimeEkleButonu.move(160, 400)
        self.kelimeEkleButonu.resize(184, 34)
        self.kelimeEkleButonu.setFont(QFont('Arial', 16, weight=QFont.Bold))
        self.kelimeEkleButonu.setAutoDefault(True)
        ########################Kutu bir#############################
        self.kutu_Bir = QLabel(self.centralwidget)
        self.kutu_Bir.setPixmap(QPixmap('kutu1.png'))
        self.kutu_Bir.move(419, 18)
        #####################################################
        self.kutu_iki = QLabel(self.centralwidget)
        self.kutu_iki.setPixmap(QPixmap('kutu2__.png'))
        self.kutu_iki.move(373, 92)
        #####################################################
        self.kutu_uc = QLabel(self.centralwidget)
        self.kutu_uc.setPixmap(QPixmap('kutu3a.png'))
        self.kutu_uc.move(319, 164)
        #####################################################
        self.b2 = QCheckBox("Çeviri aracı", self.centralwidget)
        #####################################################
        AnaPencere.setCentralWidget(self.centralwidget)

    def link(self, event):
        os.startfile('https://www.turkhackteam.org/')


class KelimeEkle(object):
    def setupUi(self, AnaPencere):
        AnaPencere.setWindowTitle('Kelime Kutusu')
        AnaPencere.setGeometry(600, 150, 500, 500)
        self.centralwidget = QWidget(AnaPencere)
        AnaPencere.arkaplan = QLabel(self.centralwidget)
        AnaPencere.arkaplan.setPixmap(QPixmap('ekleArkaplan.png'))
        AnaPencere.arkaplan.resize(500, 500)
        ########################QLine Editler###################################
        self.turkce = QLineEdit(self.centralwidget)
        self.turkce.move(315, 82)
        self.turkce.returnPressed.connect(self.eklefunc)
        self.ingilizce = QLineEdit(self.centralwidget)
        self.ingilizce.move(315, 115)
        self.ingilizce.returnPressed.connect(self.eklefunc)
        #####################Ekle Butonu######################################
        AnaPencere.ekButon = QPushButton('Ekle', self.centralwidget)
        AnaPencere.ekButon.resize(222, 34)
        AnaPencere.ekButon.move(221, 155)
        AnaPencere.ekButon.setFont(QFont('Arial', 13, weight=QFont.Bold))
        AnaPencere.ekButon.setStyleSheet("QPushButton { background-color: black;color: #FFD600; }"
                      "QPushButton:pressed { background-color: #3D3D3D }")
        AnaPencere.ekButon.setAutoDefault(True)
        AnaPencere.ekButon.clicked.connect(self.eklefunc)
        ######################Geri git Butonu####################################
        self.geriButon = QPushButton('Geri git', self.centralwidget)
        self.geriButon.resize(222, 34)
        self.geriButon.move(221, 209)
        self.geriButon.setFont(QFont('Arial', 13, weight=QFont.Bold))
        self.geriButon.setStyleSheet("QPushButton { background-color: black;color: #FFD600; }"
                      "QPushButton:pressed { background-color: #3D3D3D }")
        #######################veri tabanı oluştur######################################
        vt = sqlite3.connect('kelimeler.db')
        im = vt.cursor()

        im.execute('CREATE TABLE IF NOT EXISTS kutubir (turkce TEXT, ingilizce TEXT, deger INT)')
        im.execute('CREATE TABLE IF NOT EXISTS kutuiki (turkce TEXT, ingilizce TEXT, deger INT)')
        im.execute('CREATE TABLE IF NOT EXISTS kutuuc (turkce TEXT, ingilizce TEXT, deger INT)')
        im.execute('SELECT * FROM kutubir')
        self.data = im.fetchall()
        im.execute('SELECT * FROM kutuiki')
        self.data2 = im.fetchall()
        im.execute('SELECT * FROM kutuuc')
        self.data3 = im.fetchall()

        vt.commit()
        vt.close()
        ###########################################################
        self.mevcut = QLabel('', self.centralwidget)
        self.mevcut.move(250, 30)
        self.mevcut.setFont(QFont('Arial', 13, weight=QFont.Bold))
        ###########################################################

        AnaPencere.setCentralWidget(self.centralwidget)

    def eklefunc(self):
        turkce = self.turkce.text()
        ingilizce = self.ingilizce.text()
        for i in self.data:
            if ingilizce == i[1]:
                self.mevcut.resize(300, 30)
                self.mevcut.setText('Bu kelime zaten mevcut.')
                return None
        for i in self.data2:
            if ingilizce == i[1]:
                self.mevcut.resize(300, 30)
                self.mevcut.setText('Bu kelime zaten mevcut.')
                return None
        for i in self.data3:
            if ingilizce == i[1]:
                self.mevcut.resize(300, 30)
                self.mevcut.setText('Bu kelime zaten mevcut.')
                return None
        self.mevcut.clear()
        self.turkce.clear()
        self.ingilizce.clear()
        if turkce != '' and ingilizce != '':
            vt = sqlite3.connect('kelimeler.db')
            im = vt.cursor()
            im.execute('INSERT INTO kutubir VALUES(?, ?, ?)', (turkce, ingilizce, 0))
            vt.commit()
            vt.close()


class AnaPencere(QMainWindow):
    def __init__(self, parent=None):
        super(AnaPencere, self).__init__(parent)

        self.ckontrol = False
        self.giris = Giris()
        self.kelimeEkle = KelimeEkle()
        self.kutuBir = KutuBir()
        self.kutuIki = KutuIki()
        self.kutuUc = KutuUc()
        self.baslatGiris()

    def baslatGiris(self):
        self.giris.setupUi(self)
        self.giris.kelimeEkleButonu.clicked.connect(self.baslatKelimeEkle)
        self.giris.kutu_Bir.mousePressEvent = self.baslatKutubir
        self.giris.kutu_iki.mousePressEvent = self.baslatKutuiki
        self.giris.kutu_uc.mousePressEvent = self.baslatKutuuc
        self.giris.b2.stateChanged.connect(self.pp)
        self.show()

    def pp(self):
        if self.giris.b2.isChecked():
            self.ckontrol = True
            Thread(target=self.ceviri).start()
        else:
            self.ckontrol = False

    def baslatKelimeEkle(self):
        self.kelimeEkle.setupUi(self)
        self.kelimeEkle.geriButon.clicked.connect(self.baslatGiris)
        self.show()

    def baslatKutubir(self, event):
        self.kutuBir.setupUi(self)
        self.kutuBir.tekrarla.clicked.connect(self.baslatKutubir)
        self.kutuBir.geriButon.clicked.connect(self.baslatGiris)
        self.show()

    def baslatKutuiki(self, event):
        self.kutuIki.setupUi(self)
        self.kutuIki.tekrarla.clicked.connect(self.baslatKutuiki)
        self.kutuIki.geriButon.clicked.connect(self.baslatGiris)
        self.show()

    def baslatKutuuc(self, event):
        self.kutuUc.setupUi(self)
        self.kutuUc.tekrarla.clicked.connect(self.baslatKutuuc)
        self.kutuUc.geriButon.clicked.connect(self.baslatGiris)
        self.show()

    def ceviri(self):
        copy = tk.Tk()
        copy.withdraw()
        translator = Translator()

        veri = ''
        while self.ckontrol:
            sleep(0.3)
            try:
                if veri != copy.clipboard_get():
                    veri = copy.clipboard_get()

                    ceviri = translator.translate(veri, dest='tr').text
                    print(ceviri + '\n' + '#' * 100 + '\n')

                    if name == 'posix':
                        system(f'notify-send "Çeviri" "{ceviri}"')
                    elif name == 'nt':
                        toaster.show_toast("Çeviri", ceviri, duration=5, icon_path=None)
            except:
                pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    pencere = AnaPencere()
    sys.exit(app.exec_())
