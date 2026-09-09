# Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen yhteismäärän.
# Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa.
# Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa kunnes saadaan nopan maksimisilmäluku, joka kysytään käyttäjältä ohjelman suorituksen alussa.

import random

tahkot = int(input("Anna nopan sivujen määrä: "))
def noppa(tahkot):
    return random.randint(1, tahkot)

heitot = 1
heitto = noppa(tahkot)
while heitto != tahkot:
    heitot += 1
    print(heitto)
    heitto = noppa(tahkot)
print (f"Heitit maksimiluvun: {heitto} \nTämä vaati {heitot} heittoa!")