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


inventaario = []
i = 0

def reppu():
    tavara = input ("\n lisätään tavara reppuun:")
    if tavara:
        inventaario.append(tavara)
        print (f"reppuun lisättiin: {tavara}")
    else: (" mitään ei lisätty reppuun")
    return

menu = ("\nKauppa \nReppu \nvalikko3 \nvalikko4\n ")  #\nVikatilanteissa kokeile 'apua'
menu2 = ("\nKauppa <- \nReppu <- \nvalikko3 <- \nvalikko4 <-")
nimi = (input("Anna nimesi: "))
ikä = int(input("Anna ikäsi: "))

if ikä >= 12:
    print(f"{nimi}{ikä} - Tervetuloa peliin!")
    print (menu)
    valikko = (input("\nMitäs seuraavaksi: "))
    if valikko == "Lopeta":
        print("Peli Loppuu")
    while valikko != "Lopeta": 
        if valikko == "apua": 
            print("\nValikoista saat avattua valikoita!")
            valikko = (input(f"{menu2} \nMitäs seuraavaksi?: "))
        if valikko == "käyttäjä":
            print(f"-{nimi}{ikä}-")
            valikko = (input(f"{menu} \nMitäs seuraavaksi: "))
        if valikko == "Lopeta":
            print("Peli loppuu")
        elif valikko == "Kauppa":
            while i <= 3:
                reppu()
                i += 1
            else:
                print(f"Reppusi on täynnä!")
                valikko = (input(f"{menu} \nMitäs seuraavaksi: "))
        else:
            print("Virheellinen komento, kokeile 'apua' \n")
            valikko = (input(f"{menu} \nMitäs seuraavaksi: "))
            if valikko == "Lopeta":
                print("Peli loppuu")
else:
    print("Olet liian nuori!")


      