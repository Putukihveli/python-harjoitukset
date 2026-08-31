nimet = []

nimi = input("Anna ensimmäinen nimi tai lopeta painamalla Enter: ")
while nimi != "":
    nimet.append(nimi)
    nimi = input("Anna seuraava nimi tai poista nimi: ")

while nimi == nimet:
    poista = input("Poista nimi")
    nimet.remove(nimi)

print(nimet)