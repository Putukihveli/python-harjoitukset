#Kirjoita while-toistorakennetta käyttävä ohjelma, joka tulostaa kolmella jaolliset luvut väliltä 1..1000.
import math

i = 1
while i <= 1000:
    if i % 3 == 0:
        print(i)
    i += 1 # i'n arvo muuttuu joka "kierroksen" silmukka päättyy kun se on mennyt tuhat kertaa.