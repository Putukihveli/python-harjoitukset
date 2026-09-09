# Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. 
# Ohjelma palauttaa toisen listan, joka on muuten samanlainen kuin parametrina saatu lista paitsi että siitä on karsittu pois kaikki parittomat luvut. 
# Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen jälkeen sekä alkuperäisen että karsitun listan.

import math
def lista(luvut):
    return (luvut)

luvut = []
luvut2 = []
luku = (input("Anna ensimmäinen luku tai lopeta painamalla Enter: "))
while luku != "":
    luvut.append(int(luku))
    luku = (input("Anna seuraava luku tai lopeta painamalla Enter: "))
    if luku % 2 == 0:
        luvut2.append(int(luku))


print(luvut2)
print (lista(luvut))

