import os
import random
from lxml import html
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


options = Options()
options.headless = True
COMPANY = input('Введите название компании:')
URL = 'https://www.e-disclosure.ru/poisk-po-kompaniyam'


def get_html(sleep_time=0.6):
    driver = webdriver.Chrome(executable_path='/Users/anton/PythonProjects/py4seo/chromedriver', options=options)
    driver.get(URL)
    search_elem = driver.find_element_by_xpath('//input[@name = "textfield"]')
    search_elem.send_keys(COMPANY)
    driver.find_element_by_xpath('//*[@id="butt"]').click()
    sleep(sleep_time)
    source_code = driver.page_source
    return(source_code)


def get_elems():
    dom_tree = html.fromstring(get_html(sleep_time=3))
    links = dom_tree.xpath('//table[@class="zebra noBorderTbl"]/tbody/tr/td/a/@href')
    not_found = dom_tree.xpath('//div[@class="infoblock"]/text()')

    links_count = len(links)
    if links_count > 0:
        print(links)
    else: 
        print(not_found[0].replace('\n', '').strip())


get_elems()