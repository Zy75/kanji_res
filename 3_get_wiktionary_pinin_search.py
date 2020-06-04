#!/usr/bin/python3
# -*- coding: utf-8 -*-

# wiktionaryに各ピンインを持つ漢字のリストがあるので、とりあえずゲット。
# usage: python3 -u 3_get_wiktionary_pinin.search.py | tee wiktionary.txt 

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

def a_to_z_list():
  return [chr(i) for i in range(97,97+26)]

options = Options()
options.add_argument('-headless')
driver = webdriver.Firefox(options=options)

for ltr in a_to_z_list():

  driver.get("https://ja.wiktionary.org/wiki/%E4%BB%98%E9%8C%B2:%E6%BC%A2%E5%AD%97%E7%B4%A2%E5%BC%95_%E3%83%94%E3%83%B3%E3%82%A4%E3%83%B3/" + ltr)

  for elem in driver.find_elements_by_xpath('//h3/span[@class="mw-headline"]'):

    print( elem.text ) 

    for kanji in elem.find_elements_by_xpath('./ancestor::h3/following-sibling::dl[1]/dd/a') :
        print( kanji.text, end="" )
  
    print()

driver.quit()
