#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 中国の小学生が学ぶ約2500の常用漢字それぞれのピンインを、中国の辞書サイトからゲットする。
# ピンインは、一つの漢字に対して複数ある場合あり。あまり使われないピンインはじゃまなのだがどうするか。
# usage: python3 -u 2_get_cn_jiten_pinin.py | tee pinin.txt

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.add_argument('-headless')
driver = webdriver.Firefox(options=options)

with open('zh_jyouyou.txt') as f:
  lines = f.readlines()

for line_with_br in lines:

  line = line_with_br.strip()

  i = line.split()[0]
  kanji = line.split()[1]

  driver.get("http://xh.5156edu.com")

  driver.find_element_by_name('f_key').send_keys( kanji )

  driver.find_element_by_name('SearchString').click()

  try:
    spinin = driver.find_element_by_class_name('font_14').text

    print(i, kanji, spinin )
  except:
    print(i, kanji, 'failed' )

driver.quit()
