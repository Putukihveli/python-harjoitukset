#Tee luokka Kirja. Kirjalla on seuraavat ominaisuudet:
# nimi
# kirjoittaja
# sivumäärä
#Tee luokalle alustaja __init__. Tee lisäksi metodi:
#tulosta_tiedot()
#joka tulostaa kirjan tiedot. Luo ohjelmassa kaksi erilaista Kirja-oliota ja tulosta molempien tiedot metodin avulla.



class Kirja:
    def __init__(self, nimi, kirjoittaja, sivumäärä):
        self.nimi = nimi
        self.kirjoittaja = kirjoittaja
        self.sivumäärä = sivumäärä

def tulosta_tiedot():
    print(Kirja_1.nimi,Kirja_1.kirjoittaja, Kirja_1.sivumäärä)
    print(Kirja_2.nimi, Kirja_2.kirjoittaja, Kirja_2.sivumäärä)
Kirja_1 = Kirja ("Aapinen", "Aku-Ankka", 100)
Kirja_2 = Kirja ("Akua-Ankka", "Roope-Ankka", 250)

pöö = ()

tulosta_tiedot()

luvut = {1, 2, 2, 3, 3, 3}
print(luvut)
print(len(luvut))

#Useita olioita
#Tee luokka Opiskelija. Opiskelijalla on nimi ja pistemäärä.
#Luo vähintään kolme opiskelijaoliota ja tallenna ne listaan. Käy lista läpi silmukan avulla ja tulosta jokaisen
#opiskelijan nimi ja pistemäärä.
#Lisätehtävä
#Tulosta vain ne opiskelijat, joiden pistemäärä on vähintään 50.

class Opiskelija:
    def __init__(self, nimi, pistemäärä):
        self.nimi = nimi
        self.pistemäärä = pistemäärä