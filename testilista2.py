nimet = []

nimi = input("Anna ensimmäinen nimi tai lopeta painamalla Enter: ")
nimet.append(nimi)
while nimi != "":
    valinta = input("haluatko listätä vai poistaa (l tai p)")
    if(valinta=="l"):
        nimi = input("Anna seuraava nimi tai lopeta painamalla Enter: ")
        nimet.append(nimi)
    else:
        nimi = input("Anna poistettava nimi tai lopeta painamalla Enter: ")
        nimet.remove(nimi)
print (nimet)