from bs4 import BeautifulSoup
import requests

url = 'https://www.doviz.com/'

r = requests.get(url)

soup = BeautifulSoup(r.content, 'lxml')

veriler = soup.find('div', {'class': 'market-data'}).find_all('div', {'class', 'item'})

for i in veriler:
    birim = i.a.find('span', {'class': 'name'}).text
    degeri =i.a.find('span', {'class': 'value'}).text
    print(birim + ' : ' + degeri)
