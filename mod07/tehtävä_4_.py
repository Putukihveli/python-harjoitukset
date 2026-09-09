# Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. 
# Ohjelma palauttaa listassa olevien lukujen summan. 
# Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen palauttaman summan.


def lista(luvut):
    return (sum(luvut))

luvut = []

luku = input("Anna ensimmäinen luku tai lopeta painamalla Enter: ")
while luku != "":
    luvut.append(int(luku))
    luku = input("Anna seuraava luku tai lopeta painamalla Enter: ")

print(lista(luvut))













