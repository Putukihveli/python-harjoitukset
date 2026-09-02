#Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan.
# Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen.
# Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi kertaa.
# Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty. (Oikea käyttäjätunnus on python ja salasana rules).



käyttäjä = input("Anna käyttäjätunnus: ")
salasana = input("Anna salasana: ")
kysytty = 1


while käyttäjä != "python" or salasana != "rules":
    print("väärä")
    käyttäjä = input("Anna käyttäjätunnus: ")
    salasana = input("Anna salasana: ")
    kysytty = kysytty + 1
    if kysytty == 5:
        print("Pääsy evätty")
        break
else:
    print ("Tervetuloa")

