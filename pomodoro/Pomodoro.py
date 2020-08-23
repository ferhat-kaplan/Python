import tkinter as tk
import playsound


class Pomodoro:
    def __init__(self):
        self.kontrol = False
        self.say = 1500
        self.pencere = tk.Tk()
        self.pencere.title('Pomodoro')
        self.pencere.resizable(width=False, height=False)
        self.pencere.geometry('412x510')

        self.c = tk.Canvas(bg='white', width=512, height=512)
        self.c.place(x=0, y=0)

        self.dosya = tk.PhotoImage(file='ss2.png')
        self.imaj = self.c.create_image(210, 256, image=self.dosya)

        self.yazı = tk.Label(text='Hazır', bg='white', fg='black', font='Verdana 16 bold')
        self.yazı.place(x=175, y=40)

        self.labelOlustur()
        self.butOlustur1()
        self.pencere.mainloop()

    def labelOlustur(self):
        self.lsn = tk.Label(text='00', bg='#c31c28', fg='white', font='Verdana 22 bold')
        self.lsn.place(x=240, y=233)

        self.ldk = tk.Label(text='25', bg='#c31c28', fg='white', font='Verdana 22 bold')
        self.ldk.place(x=132, y=235)

    def butOlustur1(self):
        self.icon2 = tk.PhotoImage(file='icon2.png')
        self.b1 = tk.Button(text='başla', bg='yellow', image=self.icon2, command=self.komut)
        self.b1.place(x=190, y=450)

    def butOlustur(self):
        self.icon = tk.PhotoImage(file='icon.png')
        self.b2 = tk.Button(text='başla', bg='yellow', image=self.icon, command=self.durdur)
        self.b2.place(x=190, y=450)

    def durdur(self):
        self.b2.destroy()
        self.lsn.destroy()
        self.ldk.destroy()

        self.labelOlustur()
        self.kontrol = True
        self.butOlustur1()
        self.dosya = tk.PhotoImage(file='ss1.png')
        self.imaj = self.c.create_image(210, 256, image=self.dosya)
        self.yazı['text'] = 'Hazır'
        self.yazı['bg'] = '#515151'
        self.yazı['fg'] = 'white'


    def calısEkran(self):
        self.dosya['file'] = 'ss.png'
        self.yazı['text'] = 'Çalış'
        self.yazı['bg'] = '#ff8500'
        self.yazı['fg'] = 'white'

        self.b1.destroy()
        playsound.playsound('Basla.mp3', True)
        self.butOlustur()

    def wait(f):
        def start(*args, **kwargs):
            g = f(*args, **kwargs)
            widget = next(g)

            def repeater():
                try:

                    widget.after(next(g) * 1000, repeater)
                except StopIteration:
                    pass

            repeater()

        return start

    @wait
    def komut(self):
        self.kontrol = False
        self.calısEkran()

        yield self.pencere
        for i in range(self.say, -1, -1):
            if self.kontrol:
                break
            self.lsn["text"] = str(i % 60).zfill(2)
            self.ldk['text'] = str(i // 60).zfill(2)
            if i == 0:
                self.b2.destroy()
                self.butOlustur1()
                self.dosya = tk.PhotoImage(file='ss1.png')
                self.imaj = self.c.create_image(210, 256, image=self.dosya)
                playsound.playsound('BitisSes.mp3', True)
                self.yazı['text'] = 'Bitti'
                self.yazı['bg'] = '#515151'
                self.yazı['fg'] = 'white'

            yield 1


Pomodoro()