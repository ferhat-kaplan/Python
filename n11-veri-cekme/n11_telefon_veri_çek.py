import requests
from bs4 import BeautifulSoup
sayac = 1
sayac2 = 0
while True:
    url = "https://www.n11.com/telefon-ve-aksesuarlari/cep-telefonu?pg=" + str(sayac)
    sayac += 1

    r = requests.get(url)

    if r.url == "https://www.n11.com/telefon-ve-aksesuarlari/cep-telefonu":
        break

    soup = BeautifulSoup(r.content, 'lxml')
    sayfa = soup.find_all('li', {'class': 'column'})

    for i in sayfa:
        urun_url = i.a.get('href')
        urun_ismi = i.a.get('title')

        r2 = requests.get(urun_url)
        soup2 = BeautifulSoup(r2.content, 'lxml')
        sayac2 += 1
        print('Ürün ismi : {}'.format(urun_ismi))
        ozellik = soup2.find('div', {'class': 'unf-prop-context'}).ul.find_all('li')

        for k in ozellik:
            ozellik_ismi = k.find_all('p')[0].text
            ozellik_degeri = k.find_all('p')[1].text
            print(ozellik_ismi + ' : ' + ozellik_degeri)
        print('ürün sayısı : ', sayac2, '#'*100)
     
