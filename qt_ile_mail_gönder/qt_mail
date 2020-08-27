import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from PyQt5 import QtWidgets
import sys


class Pencere(QtWidgets.QWidget):
    def __init__(self):

        super().__init__()

        self.ui()

    def ui(self):
        self.alıcı = QtWidgets.QLineEdit()
        self.alıcı_yazısı = QtWidgets.QLabel('Alıcı mail adresi')
        self.mail_konusu = QtWidgets.QLineEdit()
        self.mail_konusu_yazisi = QtWidgets.QLabel('Mail konusu     ')
        self.mail_içeriği = QtWidgets.QTextEdit()
        self.mail_içeriği_yazısı = QtWidgets.QLabel('Mail içeriği       ')
        self.mail_adresiniz = QtWidgets.QLineEdit()
        self.mail_adresiniz_yazısı = QtWidgets.QLabel('Mail adresiniz  ')
        self.sifreniz = QtWidgets.QLineEdit()
        self.sifreniz.setEchoMode(QtWidgets.QLineEdit.Password)
        self.sifreniz_yazısı = QtWidgets.QLabel('Şifreniz           ')
        self.button = QtWidgets.QPushButton('Gönder')
        self.g_yazi = QtWidgets.QLabel('')

        h1_box = QtWidgets.QHBoxLayout()

        h1_box.addWidget(self.alıcı_yazısı)
        h1_box.addWidget(self.alıcı)

        h2_box = QtWidgets.QHBoxLayout()

        h2_box.addWidget(self.mail_konusu_yazisi)
        h2_box.addWidget(self.mail_konusu)

        h3_box = QtWidgets.QHBoxLayout()

        h3_box.addWidget(self.mail_içeriği_yazısı)
        h3_box.addWidget(self.mail_içeriği)

        h4_box = QtWidgets.QHBoxLayout()

        h4_box.addWidget(self.mail_adresiniz_yazısı)
        h4_box.addWidget(self.mail_adresiniz)

        h5_box = QtWidgets.QHBoxLayout()

        h5_box.addWidget(self.sifreniz_yazısı)
        h5_box.addWidget(self.sifreniz)

        h6_box = QtWidgets.QHBoxLayout()

        h6_box.addWidget(self.button)

        h7_box = QtWidgets.QHBoxLayout()

        h7_box.addWidget(self.g_yazi)

        v_box = QtWidgets.QVBoxLayout()

        v_box.addLayout(h1_box)
        v_box.addLayout(h2_box)
        v_box.addLayout(h3_box)
        v_box.addLayout(h4_box)
        v_box.addLayout(h5_box)
        v_box.addLayout(h6_box)
        v_box.addLayout(h7_box)

        self.setLayout(v_box)

        self.button.clicked.connect(self.mail)

        self.show()

    def mail(self):
        mesaj = MIMEMultipart()

        mesaj["Subject"] = self.mail_konusu.text()

        yazi = self.mail_içeriği.toPlainText()

        mesaj_govdesi = MIMEText(yazi, 'plain')

        mesaj.attach(mesaj_govdesi)

        try:
            mail = smtplib.SMTP('smtp.gmail.com', 587)

            mail.ehlo()
            mail.starttls()
            mail.login(self.mail_adresiniz.text(), self.sifreniz.text())

            mail.sendmail(self.mail_adresiniz.text(), self.alıcı.text(), mesaj.as_string())
            self.g_yazi.setText('Mail gönderildi.')
            mail.close()
        except:
            self.g_yazi.setText('Bir hata oluştu.')


app = QtWidgets.QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())
