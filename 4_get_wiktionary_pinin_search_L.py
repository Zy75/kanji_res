#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Lだけページの構造が違うので特別にゲット
# usage: python3 -u 4_get_wiktionary_pinin_search_L.py | tee wiktionary_L.txt

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.add_argument('-headless')
driver = webdriver.Firefox(options=options)

driver.get("https://ja.wiktionary.org/wiki/%E4%BB%98%E9%8C%B2:%E6%BC%A2%E5%AD%97%E7%B4%A2%E5%BC%95_%E3%83%94%E3%83%B3%E3%82%A4%E3%83%B3/l")

for elem in driver.find_elements_by_xpath('//h4/span[@class="mw-headline"]'):

  print( elem.text ) 

  for kanji in elem.find_elements_by_xpath('./ancestor::h4/following-sibling::dl[1]/dd/a') :
      print( kanji.text, end="" )
 
  print()

driver.quit()
