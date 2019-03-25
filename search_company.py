import os
import random
from lxml import html
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


options = Options()
options.headless = True

# def get_html():

COMPANY = input('Введите название компании:')
URL = 'https://www.e-disclosure.ru/poisk-po-kompaniyam'

driver = webdriver.Chrome(executable_path='/Users/anton/PythonProjects/py4seo/chromedriver', options=options)
driver.get(URL)

search_elem = driver.find_element_by_xpath('//input[@name = "textfield"]')
search_elem.send_keys(COMPANY)
driver.find_element_by_xpath('//*[@id="butt"]').click()
sleep(0.6)
source_code = driver.page_source
dom_tree = html.fromstring(source_code)
links = dom_tree.xpath('//table[@class="zebra noBorderTbl"]/tbody/tr/td/a/@href')
not_found = dom_tree.xpath('//div[@class="infoblock"]/text()')

links_count = len(links)
if links_count > 0:
    print(links)
elif links_count = 0:

else: 
    print(not_found[0].replace('\n', '').strip())

# Добавить проверку: если приходит пустой список, отправлять повторный запрос с увеличенным sleep на 0.1