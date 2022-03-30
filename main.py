import requests
import re

url = 'https://flip.ro/magazin/xiaomi/telefon-mobil-xiaomi-mi-10t-pro-5g-128gb-cosmic-black/72492/?conditie=Foarte%20Bun&operator=Deblocat'

r = requests.get(url)

r.content
page_source = r.content
page_source = page_source.decode("utf-8")


#get the advertised price  of the phone - in priceF
Lei3 = page_source.find('Lei ', page_source.find('Lei ', page_source.find('Lei ') + 1) + 1)
priceF = page_source[Lei3 - 5:Lei3 + 3]
priceF = re.sub("[^\d\.]", "", priceF)
priceF = int(priceF)


#get the retail price of the phone
Lei6 = page_source.find('Pret retail')
priceR = page_source[Lei6 - 48:Lei6 + 13]
priceR = re.sub("^[^\>]+", "", priceR)
priceR = re.sub(r',', "", priceR)
priceR = priceR[0:10]
priceR = re.sub("[^\d\.]", "", priceR)
priceR = priceR[0:priceR.find('.')]
priceR = int(priceR)


#get name
nm = page_source.find('Telefon mobil')
name = page_source[nm:nm + 300]
name = re.sub("\<(.*)", "", name)
name = name.rstrip()
