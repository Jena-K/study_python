import requests
from bs4 import BeautifulSoup
url = 'https://comic.naver.com/webtoon/list.nhn?titleId=183559&weekday=mon'
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')

#전체 목록 가져오기
cartoons = soup.find_all('div', attrs={'class':'rating_type'})
SUM = 0
#class 속성이 title 인 모든 'a' element 를 반환
for cartoon in cartoons:
    #title = cartoon.a.get_text()
    #print(title)

    #link = cartoon.a['href']
    #print(title, 'https://comic.naver.com'+link)

    rate = cartoon.find('strong').get_text()
    SUM += float(rate)
AVG = SUM/len(cartoons)
print(f'SUM: {SUM:0.2f}')#, SUM)
print(f'AVG: {AVG:0.2f}')#, AVG)
    