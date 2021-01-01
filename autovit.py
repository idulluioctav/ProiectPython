import requests
import json
from bs4 import BeautifulSoup


URL = 'https://autovit.ro'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
anuntZilnic = soup.find(class_='css-4i6s0 ehg01po0')
linkMasina = anuntZilnic.find('a')['href']
newURL = linkMasina
newPage = requests.get(newURL)
newSoup = BeautifulSoup(newPage.content, 'html.parser')
numeMasina = newSoup.find('h1', class_='offer-title big-text')
detalii = newSoup.find('span', class_='offer-main-params')
pret = newSoup.find('div', class_='wrapper has-price-evaluation')
detaliiJSON = numeMasina.text.split() + detalii.text.replace(" ", "").split() + pret.text.replace(" ", "").split()
with open(r'autovit.json', 'a') as jsonfile:
    json.dump(detaliiJSON, jsonfile)
    jsonfile.write('\n')