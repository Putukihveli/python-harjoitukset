#  Kirjoita Auto-luokka, jonka ominaisuuksina ovat rekisteritunnus, huippunopeus, tämänhetkinen nopeus ja kuljettu matka.
#  Kirjoita luokkaan alustaja, joka asettaa ominaisuuksista kaksi ensin mainittua parametreina saatuihin arvoihin.
#  Uuden auton nopeus ja kuljetut matka on asetettava automaattisesti nollaksi.
#  Kirjoita pääohjelma, jossa luot uuden auton (rekisteritunnus ABC-123, huippunopeus 142 km/h).
#  Tulosta pääohjelmassa sen jälkeen luodun auton kaikki ominaisuudet.



class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus, matka):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

auto = Auto("ABC-123", "142 km/h", 0, 0)

print(f"Rekisteritunnus: {auto.rekisteritunnus} Huippunopeus: {auto.huippunopeus} Nopeus: {auto.nopeus} Kuljettu matka: {auto.matka}")