from urllib.request import urlopen
from time import sleep,time
from subprocess import call
import random
import requests

url = ["https://www.google.com","https://www.facebook.com"]
UYU = 15
yazılsın_mı = False

def getUrl():
    return random.choice(url)

def baglanti_kontrol():
    try:
        çöp = requests.get(getUrl(),timeout=10)
        return True, None
    except Exception as veri:
        return False,  veri

def baglantı_kontrol2():
    try:
        urlopen(getUrl())
        return True, None
    except Exception as veri:
        return False, veri

if __name__ == "__main__":
    sayac=-1
    zaman = time()
    while True:
        print(f"{time() - zaman:.2f}", end=' ', flush=True)
        chk, veri = baglanti_kontrol()
        if chk:
            cumle = "İnternet bağlantısı kuruldu!"
            call(["espeak", "-v", "tr", cumle])
            print("İnternet bağlantısı kuruldu!")
        else:
            sayac+=1
            if sayac>=3:
                cumle = "Hâlâ, internet bağlantısı kurulamadı!"
                print(cumle)
                sayac=0
            if yazılsın_mı:
                print(f"hata: {veri}")
        sleep(UYU)
