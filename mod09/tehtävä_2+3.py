#Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi, joka saa parametrinaan nopeuden muutoksen (km/h).
#  Jos nopeuden muutos on negatiivinen, auto hidastaa. Metodin on muutettava auto-olion nopeus-ominaisuuden arvoa.
#  Auton nopeus ei saa kasvaa huippunopeutta suuremmaksi eikä alentua nollaa pienemmäksi.
#  Jatka pääohjelmaa siten, että auton nopeutta nostetaan ensin +30 km/h, sitten +70 km/h ja lopuksi +50 km/h.
#  Tulosta tämän jälkeen auton nopeus. Tee sitten hätäjarrutus määräämällä nopeuden muutos -200 km/h ja tulosta uusi nopeus.
#  Kuljettua matkaa ei tarvitse vielä päivittää.

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus, matka):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 50

    def kiihdytä(self, kmh):
        uusi_nopeus = self.nopeus + kmh

        if uusi_nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif uusi_nopeus < 0:
            self.nopeus = 0
        else:
            self.nopeus = uusi_nopeus


    def kulje(self,tunti):
            uusi_matka = self.nopeus * tunti
            self.matka = uusi_matka + self.matka
        

        

auto = Auto("ABC-123", 142,0,0)
print(f"Rekisteritunnus: {auto.rekisteritunnus} Huippunopeus: {auto.huippunopeus} Nopeus: {auto.nopeus} Kuljettu matka: {auto.matka}\n") 

print("Auton nopeus kasvaa 30km/h")
auto.kiihdytä(30)
auto.kulje(1)
print(f"Huippunopeus: {auto.huippunopeus} Nopeus: {auto.nopeus} Kuljettu matka: {auto.matka}\n" )

print("Auton nopeus kasvaa 70km/h")
auto.kiihdytä(70)
auto.kulje(1)
print(f"Huippunopeus: {auto.huippunopeus} Nopeus: {auto.nopeus} Kuljettu matka: {auto.matka}\n")

print("Auton nopeus kasvaa 50km/h")
auto.kiihdytä(50)
auto.kulje(1)
print(f"Huippunopeus: {auto.huippunopeus} Nopeus: {auto.nopeus} Kuljettu matka: {auto.matka}\n")

print("Jumalauta peura! Jarruta!")
auto.kiihdytä(-200)
print(f"Huippunopeus: {auto.huippunopeus} Nopeus: {auto.nopeus} Kuljettu matka: {auto.matka}\n")