import requests
from bs4 import BeautifulSoup
url = 'https://comic.naver.com/webtoon/weekday.nhn'
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')

#print(soup.title)  #타이틀 정보
#print(soup.title.get_text())
#print(soup.a)      #soup 객체에서 처음 발견되는 a element
#print(soup.a.attrs) #a element의 속성 정보
#print(soup.a['href'])#a-element-href 속성 값

#print(soup.find('a', attrs={'class':'Nbtn_upload'})) #class='Nbtn_upload 인 a element를 찾아줘
#print(soup.find(attrs={'class':'Nbtn_upload'})) #class='Nbtn_upload 인 any element를 찾아줘

rank1 = soup.find('li', attrs={'class':'rank01'})
#print(rank1.a.get_text())

#rank2 = rank1.next_sibling.next_sibling # 다다음 객체
#rank3 = rank2.next_sibling.next_sibling
#print(rank2)
#print(rank3)
#rank2pre = rank3.previous_sibling.previous_sibling #이 전 객체
#rank2p = rank3.parent
#print(rank2pre)

rank2 = rank1.find_next_sibling('li')
print(rank2.a.get_text())


