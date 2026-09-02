#Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän. 
# Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan. Käytä for-toistorakennetta.

import random
summa = 0
kerrat = int(input("Montako kertaa noppaa heitetään: "))
for i in range(kerrat):
    noppa = random.randint(1, 6)
    summa += noppa

print(f"Noppien summa yhteensä on: {summa}")