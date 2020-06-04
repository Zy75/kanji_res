#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 漢和辞典のサイトから漢字の音読みをゲット。ページを入ったり戻ったり。
# 途中で止まった時は、start変数を変えて再開。始めはstart=0

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys

import time 
options = Options()
options.add_argument('-headless')
driver = webdriver.Firefox(options=options)

driver.get("https://kanji.jitenon.jp/")

driver.find_element_by_id("select_search").click()

driver.find_elements_by_id("sel12")[1].click()

with open('zh_jyouyou.txt') as f:
  lines = f.readlines()

j = 0

start = 0

for line_with_br in lines:

  j += 1

  if start > j:
      continue

  line = line_with_br.strip()

  kanji = line.split()[1]  

  driver.find_elements_by_id("head_value")[1].send_keys( Keys.BACK_SPACE )
  driver.find_elements_by_id("head_value")[1].send_keys( kanji )

  driver.find_elements_by_id("head_submit")[1].click()

  elems = driver.find_elements_by_xpath('//tbody[contains(*,"音読み")]/tr/td/a')

  try:
    num_onyomi = driver.find_element_by_xpath('//th[contains(text(),"音読み")]').get_attribute("rowspan")
  except:
    print( "ERROR" )
    continue

  if num_onyomi == None:
    num_onyomi = "1"

  print( j, kanji, end=" " )
  
  for i in range(int(num_onyomi)):

    onyomi = elems[i].text
      
    print( onyomi, end=" " )

  print()  
    
  driver.back()

driver.quit()
