from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from pytube import Playlist
from pytube import YouTube
import sys


class Pencere(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setUI()

    def setUI(self):
        self.baslık()
        self.show()
        self.anaMen()

    def downvideo(self):
        url2 = self.link.text()
        YouTube(url2).streams[0].download()
        print('İndirme tamamlandı')

    def downsound(self):
        url = self.link.text()
        YouTube(url).streams.filter(type='audio')[0].download()
        print('İndirme tamamlandı')

    def baslık(self):
        self.setWindowTitle('THT youtube mp3 indirici')
        self.setGeometry(200, 200, 700, 80)

    def anaMen(self):
        widget = QWidget()

        horizantalBox = QHBoxLayout()

        text1 = QLabel('<b>Linki giriniz : </b>')
        self.link = QLineEdit()
        button = QPushButton('SES İNDİR')
        button2 = QPushButton('VİDEO İNDİR')

        button.clicked.connect(self.downsound)
        button2.clicked.connect(self.downvideo)

        horizantalBox.addWidget(text1)
        horizantalBox.addWidget(self.link)
        horizantalBox.addWidget(button)
        horizantalBox.addWidget(button2)

        widget.setLayout(horizantalBox)
        self.setCentralWidget(widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    pencere = Pencere()
    sys.exit(app.exec())
