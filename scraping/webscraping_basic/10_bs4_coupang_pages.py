from bs4 import BeautifulSoup
import requests
import re


for n in range(1, 6):
    url = f"https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={n}&rocketAll=false&searchIndexingToken=1=4&backgroundColor="
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36'}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')

    items = soup.find_all('li', attrs={'class':re.compile("^search-product")})

    for item in items:

        #If it is AD, SKIP
        ad_badge = item.find('span', attrs={'class':'ad-badge-text'})
        if ad_badge :
            print('It is AD. skip.\n')
            continue

        name = item.find('div', attrs={'class':'name'}).get_text()
        if 'Apple' in name :
            print('It is Apple product. skip.\n')
            continue

        price = item.find('strong', attrs={'class':'price-value'}).get_text()

        rate = item.find('em', attrs={'class':'rating'})
        if not rate : 
            'Have no Rate. skip.\n'
            continue
        else :
            rate = float(rate.get_text())

        review = item.find('span', attrs={'class':'rating-total-count'})#.get_text()
        if not review : 
            review = 'Have no review. skip.\n'
            continue
        else :
            review = int(review.get_text()[1:-1])

        link = item.find('a', attrs={'class':'search-product-link'})['href']
        
        print(f'Name\t:{name}')
        print(f'Price\t: {price}원')
        print(f'Rate\t: {rate}점')
        print('바로가기: {}'.format('https://www.coupang.com'+link))
        #print(f'review\t: {review}개')
        print('-'*100)