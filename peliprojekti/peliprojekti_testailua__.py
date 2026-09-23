#Projekti 1. Ohjelmointiprojektitehtävän aloitus
#
#Luo pelille oma kansio peliprojekti/ python-harjoitusprojektin sisälle ja sen sisälle readme.md-tiedosto. 
# Lisää tiedostoon otsikoksi pelisi nimi ja alle oma nimesi.
#1. Tee kansioon ohjelma, joka kysyy pelaajan nimen ja iän, tallentaa nämä muuttujiin ja tulostaa konsoliin.

#Projekti 2. Päävalikko
#
#  Muokkaa peliprojektiohjelmaa niin, että jos käyttäjä syöttää iän, joka on alle 12 v., ohjelma ilmoittaa alaikäisyydestä ja sammuu. Muussa tapauksessa ohjelma tervehtii käyttäjää, tulostaa päävalikon ja kysyy-
#  komentoja, kunnes käyttäjä kirjoittaa “lopeta”.
#  Lisää muutama keksitty komento, jotka antavat keskenään erilaisen tulosteen konsoliin. Komennon jälkeen tulostetaan valikko aina uudelleen.

#Projekti 3. Päävalikon toiminnot ja “inventaario”
#    Kehitä peliprojektia eteenpäin: Luo jokaiselle päävalikon toiminnolle (joita vähintään kolme) oma funktio, joka suoritetaan, 
#      kun käyttäjä valitsee kyseisen toiminnon.
#   Yhden funktion pitää kysyä käyttäjältä asioita (esim. esine), jotka lisätään listamuuttujaan.
#   Toisen funktion pitää tulostaa listan sisältö käyttäjälle.
#   Muut toiminnot voi ideoida ja toteuttaa vapaasti.
import random
import math

inventaario = []
i = 0

def reppu():

    tavara = input ("\nLisätään tavara reppuun:")
    if tavara:
        inventaario.append(tavara)
        print (f"Reppuun lisättiin: {tavara}")
    return

def tavarat():
    print (f"Repussasi on: {inventaario}")
    return


class Humanoidi:
     def __init__(self, nimi, ikä,):
        self.nimi = nimi
        self.ikä = ikä
        self.hp = 30

class Pelaaja(Humanoidi):
     def __init__(self, nimi, ikä,):
        super().__init__(nimi, ikä,)
        self.inventaario = []
        self.hp = 50

class Esine:
     def __init__(self, nimi, paino,):
        self.nimi = nimi
        self.paino = paino

class Miekka(Esine):
    def __init__(self,nimi,paino,vahinko):
        super().__init__(nimi, paino,)
        self.vahinko = random.randint(3-12)

class Huone:
    def __init__(self,nimi,valaistus,):
        self.nimi = nimi
        self.valaistus = valaistus
        self.tavarat = []


menu = ("\nKauppa \nReppu \nvalikko3 \nvalikko4\n ")  #\nVikatilanteissa kokeile 'apua'
menu2 = ("\nKauppa <- \nReppu <- \nvalikko3 <- \nvalikko4 <- \n")
nimi_1 = (input("Anna nimesi: "))
ikä_1 = int(input("Anna ikäsi: "))

pelaaja1 = Pelaaja(nimi_1, ikä_1)


if ikä_1 >= 12:
    print(f"{nimi_1}{ikä_1} - Tervetuloa peliin!")
    print (menu)
    valikko = (input("Mitäs seuraavaksi: "))
    while valikko != "Lopeta": 
        if not valikko: #muistutus. if not valikko: on sama kuin, if valikko == "": .The not keyword is a logical operator, and is used to reverse the result of the conditional statement:. -> Normaalist tyhjä str = False. not komento kääntää tämän toisinpäin jolloinka False -> True ja if silmukka etenee.
             print("Et syöttänyt mitään")
             valikko = (input(f"{menu} \nMitäs seuraavaksi: "))
        elif valikko == "apua": 
            print("\nValikoista saat avattua valikoita!")
            valikko = (input(f"{menu2} \nMitäs seuraavaksi?: "))
        if valikko == "käyttäjä":
            print (f"\n{pelaaja1.nimi}{pelaaja1.ikä}\nElämäpisteet: {pelaaja1.hp}")
            valikko = (input(f"{menu} \nMitäs seuraavaksi: "))
        if valikko == "Kauppa" and len(inventaario) != 4:
            print("Saat lisätä neljä tuotetta reppuusi")
            while i <= 3:
                reppu()
                i += 1
        if valikko == "Kauppa" and len(inventaario) == 4:
            print(f"Reppusi on täynnä, ehkä voisimmeme palata kauppaan myöhemmin uudestaan?")
            valikko = (input(f"{menu} \nMitäs seuraavaksi: "))
        
        if valikko == "Reppu":
            tavarat()
            valikko = (input(f"{menu} \nMitäs seuraavaksi: "))
        if valikko == "Lopeta":
            print("Peli Loppuu")
        else:
            print("Tuntematon komento!")
            valikko = (input(f"{menu2} \nMitäs seuraavaksi?: "))
                
else:
    print("Olet liian nuori!")



       #while i <= 3:
       #               reppu()
       #               i += 1
       #               print(f"Reppusi on täynnä!")
        #          valikko = (input(f"{menu} \nMitäs seuraavaksi: "))