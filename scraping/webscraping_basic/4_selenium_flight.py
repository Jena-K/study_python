from selenium import webdriver
from selenium.webdriver.common.by import by
from selenium.webdriver.comon.by import by

import time

browser = webdriver.Chrome()
#browser.maximize_window()
url = 'https://flight.naver.com/flights/'

#url로 이동
browser.get(url)

#가는 날 선택 클릭
browser.find_element_by_link_text('가는날 선택').click()

# 이번 달 27, 28일 선택
#browser.find_elements_by_link_text('27')[0].click()
#browser.find_elements_by_link_text('28')[0].click()

# 다음 달 27, 28일 선택
#browser.find_elements_by_link_text('27')[1].click()
#browser.find_elements_by_link_text('28')[1].click()

# 이번 달 27, 28일 선택
browser.find_elements_by_link_text('27')[0].click()
browser.find_elements_by_link_text('28')[1].click()

# 제주도 선택
browser.find_element_by_xpath('//*[@id="recommendationList"]/ul/li[1]/div/span').click()

# 항공권 검색
browser.find_element_by_link_text('항공권 검색').click()

time.sleep(10)
# 검색 결과
elem = browser.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[4]/ul/li[1]')
print(elem.text)
time.sleep(100)