#!/usr/bin/python3
# -*- coding: utf-8 -*-

# check

with open('wiktionary_complete.txt') as f_wiki:
  lines_wiki = f_wiki.readlines()

with open('pinin_table.txt') as f_table:
  lines_table = f_table.readlines()

list_spin = [ line_with_br.strip().split()[0] for line_with_br in lines_table ]

i = 0

for line_with_br in lines_wiki:

  i += 1

  if i % 2 == 1:
    line = line_with_br.strip()
 
    found = 0

    for spin in list_spin:

      if line == spin:
         found = 1
         break

    if found == 1:
      print( "OK", line )
    else:
      print( "BAD", line )
