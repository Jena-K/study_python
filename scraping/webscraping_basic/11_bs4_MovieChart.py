import requests
from bs4 import BeautifulSoup
import re
import os

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36'}

for year in range(2015, 2021):
    if not os.path.isdir(str(year)):
        os.mkdir(str(year))
    url = f'https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q={year}+%EB%B0%95%EC%8A%A4%EC%98%A4%ED%94%BC%EC%8A%A4'
    
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')

    images = soup.find_all('img', attrs={'class':'thumb_img'})
    for idx, image in enumerate(images) :
        if idx >= 5 : break
        image_url = image['src']
        if image_url.startswith('//'):
            image_url = 'https:' + image_url

        print(image_url)
        image_res = requests.get(image_url)
        image_res.raise_for_status()

        
        with open('{}\\movie{}.jpg'.format(year, idx+1), 'wb') as f:
            f.write(image_res.content)

    # items = soup.find_all('div', attrs={'class':'wrap_cont cont_type2'})
    # for item in items:
    #     print(f"Movie\t: {item.find('a', attrs={'class':'tit_main'}).get_text()}")

    #     rate = item.find('em', attrs={'class':'rate'}).get_text()
    #     if not rate :
    #         rate = 'NO RATE!'
    #     print(f"Rate\t: {rate}")

    #     book = item.find('dd', attrs={'class':'cont'}).get_text()
    #     print(f'Book\t: {book}')


    #        print('-'*100)