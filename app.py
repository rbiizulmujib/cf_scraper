import requests
from bs4 import BeautifulSoup as bs
from random import randint
from time import sleep

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.50'}
URL = input('Masukan URL:')

namafile = input('Simpan dengan nama:')
jumlah_halaman = int(input('Mau berapa halaman?:'))
jumlah_halaman += 1
output=open(namafile + ".txt", "w")


for page in range(1, jumlah_halaman):
    req = requests.get(URL + str(page), headers=headers)
    soup = bs(req.text, 'html.parser')
    
    for link in soup.findAll('img', src=True):
        imagelinks = link.get('src').replace('https://www.facebook.com/tr?id=1104013239621163&ev=PageView&noscript=1', '').replace('https://www.creativefabrica.com/wp-content/themes/creativefabricanew/v2.0/images/powered-b.png', '')
        #print(imagelinks[:-12]+(imagelinks[-4:]))
        output.write(imagelinks[:-12]+(imagelinks[-4:]) + '\n')

    print('Url link:', URL + str(page), '🔥') 
    print('Memproses halaman ' + str(page), 'berhasil ✅')

output.flush()
output.close
