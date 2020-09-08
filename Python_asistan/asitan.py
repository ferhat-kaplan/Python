import speech_recognition as sr
import os, re, json
from youtubesearchpython import SearchVideos
import json
import io
import pygame
from gtts import gTTS

r = sr.Recognizer()


def dinle():
    with sr.Microphone() as source:
        print("Konuş güzel kardeşim :")
        audio = r.listen(source)
        ses = str(r.recognize_google(audio, language="tr"))
        ses = ses.lower()
        print("Şöyle dediniz:" + ses)
        print(type(ses))
        if 'lan' in ses:
            if "youtube'dan" in ses and 'aç' in ses:
                derle = re.compile("youtube'dan (.*).*aç")
                sonuc = derle.search(ses)
                os.startfile(yAra(sonuc.group(1)))
                öt(sonuc.group(1) + ' açıldı')
            elif 'nasılsın' in ses:
                öt('Sanane lan gevşek')


def yAra(ara):
    search = SearchVideos(ara, offset=1, mode="json", max_results=20)
    deneme = json.loads(search.result())
    return deneme['search_result'][0]['link']


def öt(fesatlıklar):
    with io.BytesIO() as f:
        gTTS(text=fesatlıklar, lang='tr').write_to_fp(f)
        f.seek(0)
        pygame.mixer.init()
        pygame.mixer.music.load(f)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue


while True:
    try:
        dinle()
    except:
        print('Anlayamadım')
