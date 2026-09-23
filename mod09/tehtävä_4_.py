#   Nyt ohjelmoidaan autokilpailu. Uuden auton kuljettu matka alustetaan automaattisesti nollaksi. 
#   Tee pääohjelman alussa lista, joka koostuu kymmenestä toistorakenteella luodusta auto-oliosta. 
#   Jokaisen auton huippunopeus arvotaan 100 km/h ja 200 km/h väliltä. Rekisteritunnus luodaan seuraavasti “ABC-1”, “ABC-2” jne. Sitten kilpailu alkaa. 
#   Kilpailun aikana tehdään tunnin välein seuraavat toimenpiteet:
#   Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos arvotaan väliltä -10 ja +15 km/h väliltä. Tämä tehdään kutsumalla kiihdytä-metodia.
#   Kaikkia autoja käsketään liikkumaan yhden tunnin ajan. Tämä tehdään kutsumalla kulje-metodia.
#   Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä. Lopuksi tulostetaan kunkin auton kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna.

import random
autot = []

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus, matka):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0 

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
            self.matka = int(uusi_matka) + int(self.matka)


#auto = Auto("ABC-123", 142,0,0)

#print(f"Rekisteritunnus: {auto.rekisteritunnus} Huippunopeus: {auto.huippunopeus} Nopeus: {auto.nopeus} Kuljettu matka: {auto.matka}\n") 

for i in range(1,11):
    autot.append(Auto(f"ABC-{i}", random.randint(100,200),0,0))

#kisa_käynnissä = True

while auto.matka < 250:
    for auto in autot:
        auto.kiihdytä(random.randint(-10,15))
        auto.kulje(1)
else:
    for auto in autot:
        print(f"Rekisteritunnus: {auto.rekisteritunnus} Huippunopeus: {auto.huippunopeus} Nopeus: {auto.nopeus} Kuljettu matka: {auto.matka}") 
    print("Kisa loppui!") 


#print("Auton nopeus kasvaa 30km/h")
#auto.kiihdytä(30)
#auto.kulje(1)
#print(f"Huippunopeus: {auto.huippunopeus} Nopeus: {auto.nopeus} Kuljettu matka: {auto.matka}\n" )

#print("Auton nopeus kasvaa 70km/h")
#auto.kiihdytä(70)
#auto.kulje(1)
#print(f"Huippunopeus: {auto.huippunopeus} Nopeus: {auto.nopeus} Kuljettu matka: {auto.matka}\n")

#print("Auton nopeus kasvaa 50km/h")
#auto.kiihdytä(50)
#auto.kulje(1)
#print(f"Huippunopeus: {auto.huippunopeus} Nopeus: {auto.nopeus} Kuljettu matka: {auto.matka}\n")

#print("Jumalauta peura! Jarruta!")
#auto.kiihdytä(-200)
#print(f"Huippunopeus: {auto.huippunopeus} Nopeus: {auto.nopeus} Kuljettu matka: {auto.matka}\n")

