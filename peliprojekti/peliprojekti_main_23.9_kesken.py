
import json
import os
import random
import math
from hahmot .luokat import Pelaaja, Humanoidi,Esine,Miekka,Reppu, Huone, Luola, Kauppa
from hahmot import tavarat, reppu, tallenna

inventaario = []

i = 0
a = 0

#polku = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Save.json")

polku_intro = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Intro.txt") #__file__ = viittaa nykyiseen pythonskriptitiedostoon, os.path.abspath(__file__) > hakee skriptin absoluuttisen sijainnin.
with open (polku_intro, 'r', encoding="utf-8") as tiedosto:
    data = tiedosto.read()
    print(data)

polku_ohjeet = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Ohjeet.txt")
with open (polku_ohjeet, 'r', encoding="utf-8") as tiedosto:
    data_1 = tiedosto.read()

polku_ohjeet = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Ohjeet_2.txt")
with open (polku_ohjeet, 'r', encoding="utf-8") as tiedosto:
    data_2 = tiedosto.read()

with open("save.txt", "w") as tiedosto:
    tiedosto.write("Pelaaja pääsi tasolle 2.")

menu = ("\nOhjeet \nTiedot \nKauppa \nReppu\n ")  #\nVikatilanteissa kokeile 'apua'
menu2 = ("\nOhjeet <- \nTiedot <- \nKauppa <- \nReppu <- \n")
nimi = (input("Anna nimesi: "))
ikä_1 = int(input("Anna ikäsi: "))

pelaaja1 = Pelaaja(nimi,ikä_1,"Taverna",)
aloitus_huone = Huone("Taverna","Hämärä","Lämmin","Kaupunki")
kauppias = Kauppa("Kauppa","Kirkas","Lämmin", "Kaupunki",)
miekka = Miekka("Excalibur", ("5kg"), "4-12.")
laukku = Reppu("Säkki", 5,)

inventaario = pelaaja1.inventaario

kauppias.hylly.append(miekka)
kauppias.hylly.append(laukku)

if ikä_1 >= 12:
    print(f"\n{nimi}{ikä_1} - Tervetuloa peliin! \nSeikkailusi alkaa kaupungin lämpimästä tavernasta, mitä haluaisit tehdä seuraavaksi?")
    #print(f"{eteinen.nimi}")

    print (menu)
    valikko = (input("Mitäs seuraavaksi: "))
    while valikko != "Lopeta": 
        if not valikko: #muistutus. if not valikko: on sama kuin, if valikko == "": .The not keyword is a logical operator, and is used to reverse the result of the conditional statement:. -> Normaalist tyhjä str = False. not komento kääntää tämän toisinpäin jolloinka False -> True ja if silmukka etenee.
             print("Et syöttänyt mitään")
             valikko = (input(f"{menu} \nMitäs seuraavaksi: "))
        elif valikko == "Ohjeet" and a==0:
            print(data_1)
            valikko = (input(f"{menu} \nMitäs seuraavaksi: "))
        elif valikko == "Ohjeet" and a == 1:
            print(data_2)
            valikko = (input(f"{menu} \nMitäs seuraavaksi: "))
        elif valikko == "apua": 
            print("\nValikoista saat avattua valikoita!")
            valikko = (input(f"{menu2} \nMitäs seuraavaksi?: "))
        elif valikko == "Tiedot":
            print (f"\nNimi: {pelaaja1.nimi}{pelaaja1.ikä} \nSijainti: {pelaaja1.sijainti}\nElämäpisteet: {pelaaja1.hp}\nInventaario: {pelaaja1.inventaario}")
            valikko = (input(f"{menu} \nMitäs seuraavaksi: "))
        elif valikko == "Tallenna":
            tallenna(pelaaja1)
            print("Peli tallennettu")
            valikko = (input(f"{menu} \nMitäs seuraavaksi: "))
        elif valikko == "Kauppa" and len(inventaario) < 4:
            a = 1
            print(f"Saavut kauppaan, kauppa on {kauppias.lämpötila} ja valaistus on {kauppias.valaistus}.\nSijainti: {kauppias.sijainti}")
            print("Kauppias on kuullut tulevasta seikkailustasi. Saat lisätä neljä tuotetta reppuusi!")
            print (kauppias.hylly)
            #print(f"{miekka},\n{laukku}") #Miten saisi tulostettua koko "Kauppiaan ostoslistan ilman että tulee "<function tavarat at 0x000001C065704040>" jne.
            while len(inventaario) < 4 and len(kauppias.hylly) > 0:
                print("\n Kauppiaalla on tuotteita:", kauppias.hylly)
                reppu(kauppias, inventaario)
                if len (inventaario) == 4:
                    print("\n Kaikki tuoteett ostettu aj reppusi on nyt täysi!")
                    valikko = input(f"{menu} \nMitäs seuraavaksi: ")
        elif valikko == "Kauppa" and len(inventaario) == 4:
            print(f"Reppusi on täynnä, ehkä voisimmeme palata kauppaan myöhemmin uudestaan?.")
            valikko = (input(f"{menu} \nMitäs seuraavaksi: "))
        
        elif valikko == "Reppu":
            tavarat (pelaaja1.inventaario)
            valikko = (input(f"{menu} \nMitäs seuraavaksi: "))
        else:
            print("Tuntematon komento!")
            valikko = (input(f"{menu2} \nMitäs seuraavaksi?: "))
           
if valikko == "Lopeta":
            print("Peli Loppuu")
        
else:
    print("Olet liian nuori!")