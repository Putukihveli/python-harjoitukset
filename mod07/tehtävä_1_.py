#Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen nopan silmäluvun väliltä 1..6. 
# Kirjoita pääohjelma, joka heittää noppaa niin kauan kunnes tulee kuutonen. 
#Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.
import random

def noppa():
    return random.randint(1,6)

heitot = 1
heitto = noppa()
while heitto != 6:
    heitot += 1
    print(heitto)
    heitto = noppa()

print (f"{heitto} Heitit kuutosen! \nTämä vaati {heitot} heittoa! ")
