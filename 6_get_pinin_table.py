#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 声調記号つきのピンインと、ないピンインの対応表を作る。wiktionaryのページを使う。

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

def a_to_z_list():
  return [chr(i) for i in range(97,97+26)]

options = Options()
options.add_argument('-headless')
driver = webdriver.Firefox(options=options)

for ltr in a_to_z_list():

  driver.get("https://ja.wiktionary.org/wiki/%E4%BB%98%E9%8C%B2:%E6%BC%A2%E5%AD%97%E7%B4%A2%E5%BC%95_%E3%83%94%E3%83%B3%E3%82%A4%E3%83%B3/" + ltr)

  for elem in driver.find_elements_by_xpath('//ul/li/ul/li/a/span[@class="toctext"]'):

    elem2 = elem.find_element_by_xpath('../../../preceding-sibling::a/span[@class="toctext"]')
 
    spin = elem.text
    pin = elem2.text

    print( spin , pin )

driver.quit()
