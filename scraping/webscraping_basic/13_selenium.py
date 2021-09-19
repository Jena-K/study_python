from selenium import webdriver
import os
import time 

browser = webdriver.Chrome('./chromedriver.exe')
#1. 네이버 이동
naver = 'http://naver.com'
browser.get(naver)

#2. 로그인 페이지 이동.
elem = browser.find_element_by_class_name('link_login')
elem.click()

#3. ID, WP 입력
elem = browser.find_element_by_id('id').send_keys('my_id')
elem = browser.find_element_by_id('pw').send_keys('my_pw^')

time.sleep(1)
#4. 로그인 버튼 클릭
browser.find_element_by_id('log.login').click()

#5. ID를 새로 입력
elem = browser.find_element_by_id('id').clear()
elem = browser.find_element_by_id('id').send_keys('my_new_id')

#6. HTML 정보 출력
print(browser.page_source)

time.sleep(1)

#브라우저 종료
browser.quit()
