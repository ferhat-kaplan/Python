import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys


mesaj = MIMEMultipart()

mesaj["From"] = "gönderen mail adresi"

mesaj["To"] = "alıcı mail adresi"

mesaj["Subject"] = "mailin konusu"


yazi = """
Smtp

Bu mailimizin içeriğidir
"""


mesaj_govdesi = MIMEText(yazi, 'plain')

mesaj.attach(mesaj_govdesi)

try:
    mail = smtplib.SMTP('smtp.gmail.com', 587)

    mail.ehlo()
    mail.starttls()
    mail.login('gönderen mail adresi', 'şifre')
    while True:
        mail.sendmail(mesaj['From'], mesaj['To'], mesaj.as_string())
    print('mail başarı ile gönderildi')
    mail.close()
except:
    sys.stderr.write('bir sorun oluştu ...')
    sys.stderr.flush()
