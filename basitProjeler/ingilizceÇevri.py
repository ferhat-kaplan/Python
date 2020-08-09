import tkinter
import time
import requests
import re
import os

reg = re.compile('<td class="tr ts" lang="tr"><a href="/tr/turkce-ingilizce/[^"]+">([^<]+)</a> </td>')
clip = tkinter.Tk()
clip.withdraw()

clip_tmp = None

url = "https://tureng.com/tr/turkce-ingilizce/"

while True:
    time.sleep(0.2)
    try:
        if clip_tmp != clip.clipboard_get():
            clip_tmp = clip.clipboard_get()

            html = reg.findall(
                requests.get('https://tureng.com/tr/turkce-ingilizce/' + clip.clipboard_get().lower()).text)

            if html:
                html = html[0].replace('&#231', 'ç').replace('&#246', 'ö').replace('&#252', 'ü').replace(';', '')

                print(clip.clipboard_get(), html)
                os.system(f'notify-send "{clip_tmp.title()}" "{html.title()}"')
    except tkinter.TclError:
        pass
