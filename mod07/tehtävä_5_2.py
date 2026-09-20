# Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. 
# Ohjelma palauttaa toisen listan, joka on muuten samanlainen kuin parametrina saatu lista paitsi että siitä on karsittu pois kaikki parittomat luvut. 
# Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen jälkeen sekä alkuperäisen että karsitun listan.

import math
def jako(lista):
    uusi_lista = []
    for num in (lista):
     if num % 2 == 0:
        uusi_lista.append(num)

lista = [1,2,3,4,5]
uusi = jako(lista)
print(lista)
print(uusi)



