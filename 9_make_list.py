#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 中国語のピンインと日本語の音読の対応を出す。入力：input.txt

# 見易くするには $ tabs 32 
# usage: python3 <this script>.py

with open('input.txt') as l:
  l_lines = l.readlines()

with open('cjiten.txt') as c:
  c_lines = c.readlines()

with open('kanwa.txt') as k:
  k_lines = k.readlines()

with open('pinin_table.txt') as p:
  p_lines = p.readlines()

inp_list = [ l_line_br.strip() for l_line_br in l_lines ]

spin_pin_list = [ p_line_br.strip().split() for p_line_br in p_lines ]

cjiten_list = [ c_line_br.strip().split() for c_line_br in c_lines ]

kanwa_list = [ k_line_br.strip().split() for k_line_br in k_lines ]

#------------------------------------------------------------------------

spin_list = []

for inp in inp_list:
  
  for spin_pin in spin_pin_list:

    if inp == spin_pin[1]:
       
       spin_list.append(spin_pin[0])

def common_element(cjiten, spin_l):

  for m in range(2, len(cjiten) - 1):
    for spin in spin_l:
      
      if cjiten[m].strip(',') == spin:

        return True

  return False

for kanwa,cjiten in zip(kanwa_list,cjiten_list): 
            
  if common_element(cjiten, spin_list) == True:              
    
    kanji = cjiten[1]  

    print(kanji, end=' ')
           
    for s in range(2, len(cjiten) - 1):
          
      spin = cjiten[s].strip(',')

      print(spin , end=' ')

    print('\t', end = ' ' )

    for s in range(2, len(kanwa)):
        
      onyomi = kanwa[s]  

      print(onyomi, end=' ')

    print('')
