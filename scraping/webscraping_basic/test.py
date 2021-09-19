from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

'''
options = webdriver.ChromeOptions()
options.add_argument("start-maximized");
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
driver = webdriver.Chrome(chrome_options=options)
'''''
driver = webdriver.Chrome()

driver.get('https://www.google.com/maps/d/u/0/embed?mid=19IDHrgdt3sKCKPxpunY80_JJemo&hl=en_US&ll=35.74989748552266%2C127.88267734999997&z=7')
sleep(0.5)

driver.find_element_by_xpath('//*[@id="map-canvas"]/div[2]/div[2]/div/div[1]').click()
sleep(0.5)

elems_more = driver.find_elements_by_class_name('HzV7m-pbTTYe-bN97Pc-ti6hGc-z5C9Gb')
for elem in elems_more :
    elem.click()

elems = driver.find_elements_by_class_name('suEOdc')

regx = re.compile()
for elem in elems:
    if elem.text and elem.text[0].isdigit():
        driver.execute_script("arguments[0].click();", elem)
        driver.implicitly_wait(3)
        print(elem.text)
        try :
            place = driver.find_element_by_class_name('fO2voc-jRmmHf-MZArnb-Q7Zjwb')
        except:
            continue
        #print(place.text)

os.system('pause')
