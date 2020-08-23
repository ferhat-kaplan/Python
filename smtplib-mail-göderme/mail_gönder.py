import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys


mesaj = MIMEMultipart()

mesaj["From"] = "fkmll2121@gmail.com"

mesaj["To"] = "mekafkmll@gmail.com"

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
    mail.login('fkmll2121@gmail.com', 'lock2121')
    while True:
        mail.sendmail(mesaj['From'], mesaj['To'], mesaj.as_string())
    print('mail başarı ile gönderildi')
    mail.close()
except:
    sys.stderr.write('bir sorun oluştu ...')
    sys.stderr.flush()
