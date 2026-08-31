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

nimi = (input("Anna nimesi: "))
ikä = int(input("Anna ikäsi: "))
#print (f"Pelaaja: {nimi}{ikä}")
while ikä >= 12:
    print(f"{nimi}{ikä} - Tervetuloa peliin!")

    print("\nvalikko1 \nvalikko2 \nvalikko3 \nvalikko4")
    break
if ikä < 12: 
    print ("Alaikäikäinen, peli sulkeutuu!")
    


valikko = (input("\nMitäs seuraavaksi: "))
if valikko == "Lopeta": 
    print ("heihei!")







#elif input


      