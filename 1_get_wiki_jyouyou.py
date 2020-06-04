#!/usr/bin/python3
# -*- coding: utf-8 -*-

# wikibooksのサイトから、中国の小学生が学ぶ常用漢字2500のリストをゲット。
# usage: python3 1_get_wiki_jyouyou.py > zh_jyouyou.txt

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.add_argument('-headless')
driver = webdriver.Firefox(options=options)

driver.get("https://ja.wikibooks.org/wiki/%E4%B8%AD%E5%9B%BD%E8%AA%9E%E3%81%AE%E5%B8%B8%E7%94%A8%E6%BC%A2%E5%AD%97")

i=1

for elem in driver.find_elements_by_class_name('extiw'):
  print( i, elem.text )
  i+=1
driver.quit()
