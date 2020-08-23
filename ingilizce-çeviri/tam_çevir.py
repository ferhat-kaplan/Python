from googletrans import Translator
import tkinter as tk
from time import sleep
from os import system
from os import name
if name == 'nt':
    from win10toast import ToastNotifier
    toaster = ToastNotifier()


copy = tk.Tk()
copy.withdraw()
translator = Translator()

veri = ''
while True:
    sleep(0.3)
    try:
        if veri != copy.clipboard_get():
            veri = copy.clipboard_get()

            ceviri = translator.translate(veri, dest='tr').text
            print(ceviri + '\n' + '#'*100 + '\n')

            if name == 'posix':
                system(f'notify-send "Çeviri" "{ceviri}"')
            elif name == 'nt':
                toaster.show_toast("Çeviri", ceviri, duration=5, icon_path=".img\\22.ico")
    except:
        pass
