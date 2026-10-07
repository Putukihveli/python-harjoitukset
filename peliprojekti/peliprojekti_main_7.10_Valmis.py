import json
import os
import random
import math
from hahmot .luokat import Pelaaja, Humanoidi,Esine,Miekka,Reppu, Huone, Luola, Kauppa
from hahmot import tavarat, reppu, tallenna, print_slow
import sys,time

inventaario = []

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

menu = ("\nOhjeet \nTiedot \nKauppias \nReppu\n ")  #\nVikatilanteissa kokeile 'apua'
menu2 = ("\nOhjeet <- \nTiedot <- \nkauppias <- \nReppu <- \n")
menu3 = ("\nOhjeet \nTiedot \nKauppias \nReppu \nMetsä\n ")
menu4 = ("\nOhjeet \nTiedot \nLuola \nReppu \nKaupunki\n ")
menu_1 =("\nOhjeet \nTiedot \nLuola \nReppu \nxxx  \n ")
menu_2 =("\nTiedot \nReppu \nEteenpäin")
menu_3 =("\nLyönti \nTiedot \nReppu")
nimi = (input("\nAnna nimesi: "))
ikä_1 = int(input("Anna ikäsi: "))

pelaaja1 = Pelaaja(nimi,ikä_1,"Taverna",)
aloitus_huone = Huone("Taverna","Hämärä","Lämmin","Kaupunki")
kauppias = Kauppa("Kauppa","Kirkas","Lämmin", "Kaupunki",)
miekka = Miekka("Excalibur", "5kg", "4-12.")
laukku = Reppu("Säkki", 5,)
Metsä = Huone("Synkkämetsä","Sumuinen","Kolea","Metsä",)
Luola_1 = Luola("Kalloluola","Kylmä","Pimeä")
luuranko = Humanoidi("Skeletori",1000,{Luola_1})

inventaario = pelaaja1.inventaario

kauppias.hylly.append(miekka)
kauppias.hylly.append(laukku)

pelin_tila = 0
a = 0

if ikä_1 >= 12:
    print(f"\n{nimi}{ikä_1} - Tervetuloa peliin! \nSeikkailusi alkaa kaupungin lämpimästä tavernasta, mitä haluaisit tehdä seuraavaksi?")
    #print(f"{eteinen.nimi}")

    print (menu)
    valikko = (input("Mitäs seuraavaksi: ")) 
    while valikko != "Lopeta":
        if a == 1: menu = menu3
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
        elif valikko == "Tiedot" and pelin_tila == 0:
            print (f"\nNimi: {pelaaja1.nimi}{pelaaja1.ikä} \nSijainti: {pelaaja1.paikka}\nElämäpisteet: {pelaaja1.hp}\nInventaario: {pelaaja1.inventaario}")
            valikko = (input(f"{menu} \nMitäs seuraavaksi: "))
        elif valikko == "Tiedot" and pelin_tila == 2:
            print (f"\nNimi: {pelaaja1.nimi}{pelaaja1.ikä} \nSijainti: {pelaaja1.paikka}\nElämäpisteet: {pelaaja1.hp}\nInventaario: {pelaaja1.inventaario}")
            valikko = (input(f"{menu_2} \nMitäs seuraavaksi: "))
        elif valikko == "Tiedot" and pelin_tila == 3:
            print (f"\nNimi: {pelaaja1.nimi}{pelaaja1.ikä} \nSijainti: {pelaaja1.paikka}\nElämäpisteet: {pelaaja1.hp}\nInventaario: {pelaaja1.inventaario}")
            valikko = (input(f"{menu_3} \nMitäs seuraavaksi: "))
        elif valikko == "Tallenna":
            tallenna(pelaaja1)
            print("Peli tallennettu")
            valikko = (input(f"{menu} \nMitäs seuraavaksi: "))
        elif valikko == "Kauppias" and len(inventaario) < 4:
            a = 1
            print(f"Saavut kauppaan, kauppa on {kauppias.lämpötila} ja valaistus on {kauppias.valaistus}.\nSijainti: {kauppias.sijainti}")
            print("Kauppias on kuullut tulevasta seikkailustasi. Saat lisätä neljä tuotetta reppuusi!")
            print (kauppias.hylly)
            #print(f"{miekka},\n{laukku}") #Miten saisi tulostettua koko "Kauppiaan ostoslistan ilman että tulee "<function tavarat at 0x000001C065704040>" jne.
            while len(inventaario) < 4 and len(kauppias.hylly) > 0:
                print("\nKauppiaalla on tuotteita:", kauppias.hylly)
                reppu(kauppias, inventaario)
                if len (inventaario) == 4:
                    print("\nKaikki tuotteet on ostettu ja reppusi on nyt täysi!")
                    print_slow("\nKaupungin hälytyskellot soivat! Metsän laidalta on kuulunut kiljuntaa!") #Hidas ja dramaattinen tulostus.
                    #pelin_tila == 2
                    if a == 1: menu = menu3 # Kun kaupassa on käyty, menu vaihtuu menu3 josta löytyy mahdollisuus siirtyä metsään.
                    valikko = input(f"{menu} \nMitäs seuraavaksi: ")
        elif valikko == "Kauppias" and len(inventaario) == 4:
            print(f"Reppusi on täynnä, ehkä voisimmeme palata kauppaan myöhemmin uudestaan?.")
            valikko = (input(f"{menu} \nMitäs seuraavaksi: "))
        
        elif valikko == "Reppu" and pelin_tila == 0:
            tavarat (pelaaja1.inventaario)
            valikko = (input(f"{menu} \nMitäs seuraavaksi: "))
        #elif valikko =="Reppu" and pelin_tila == 3:
            #tavarat (pelaaja1.inventaario)
            #print(f"{pelaaja1.nimi}, Elämäpisteet: {pelaaja1.hp}")
            #print(f"{luuranko.nimi}, Elämäpisteet: {luuranko.hp}")
            #valikko = (input(f"{menu_3} \nMitäs seuraavaksi: "))
        elif valikko == "Metsä":
            valikko = input(f"Saavut kaupungin reunalla sijaitsevan {Metsä.nimi}'n laidalle. Käännytkö pelkurina takaisin vai jatkatko matkaasi syvemmälle metsään? \n| Kaupunki | | Seikkailu |: ")
            if valikko == "Kaupunki":
                print("\nOletko varma että haluat palata kaupunkiin ja jättää metsän mysteerin selvittämättä?")
                valinta2 = input("| Kaupunki | | Seikkailu |: ")
                if valinta2 == "Kaupunki":
                    print('Saavut takaisin kaupunkiin, omatuntoasi kolkuttaa..Mitä metsässä olisikaan voinut odottaa?.. \n-The End-') # 1/3 peli pelattu läpi.
                    quit()
        elif valikko == "Seikkailu":
                pelin_tila = 2 # Pelin tila päivittyy jotta myöhemmin reppu komento toimii eritavalla. Lisätty että myös tiedot komento toimii ajankohtaisesti eikä aina heitä samaa "alku" valikkoa.
                pelaaja1.vaihda_sijaintia(Metsä)
                print(f"\nMetsän reunalla huomaat että se on {Metsä.valaistus} ja {Metsä.lämpötila}. Päätät silti jatkaa matkaa. \nHetken tarpomisen jälken havahdut olevasi syvällä metsässä ja edessäsi ammotta pääkalloa muistuttavan luolan suu.")
                print(f"Astuessasi luolaan, tunnet pistävän kivun jalassasi! Olet astunut terävistä luista tehtyyn ansaan ja menetät 10 elämäpistettä.")
                pelaaja1.hp = pelaaja1.hp - 10
                pelaaja1.vaihda_sijaintia(Luola_1)
                print(f"Elämäpisteesi: {pelaaja1.hp}")
                valikko = (input(f"{menu_2} \nMitäs seuraavaksi: "))
        elif valikko == "Reppu" and "Banaani" in inventaario and (pelin_tila == 2 or pelin_tila == 3): #Repusta pystyy nyt syömään banaanin joka antaa 10 elämäpistettä.
                tavarat (pelaaja1.inventaario)
                ruokailu = input(f"Tahtoisitko kenties syödä banaanisi? Kyllä | Ei: ")
                if ruokailu == "Kyllä":
                    print("Nom Nom!")
                    pelaaja1.hp = pelaaja1.hp +15
                    print(f"Elämäpisteesi: {pelaaja1.hp}")
                    inventaario.remove("Banaani")
                    print("Muista kierrättää ja siivota kuoret ja muutkin matkalla syntyvät roskat!") #Kestävän kehityksen tavoitteet 12,13 ja 15. Muistakaa kierrättää ja siivota omat roskat!
                    tavarat(pelaaja1.inventaario)
                elif ruokailu == "Ei":
                     print("Ehkä myöhemmin")
                     tavarat(pelaaja1.inventaario)
                if pelin_tila == 2:
                     valikko = (input(f"{menu_2} \nMitäs seuraavaksi: "))
                if pelin_tila == 3:
                    valikko = (input(f"{menu_3} \nMitäs seuraavaksi: "))
        elif valikko == "Eteenpäin":
             pelin_tila = 3 # jotta repun banaanin voi syödä vielä kesken taistelun.
             print("\nJatkat matkaasi luolan uumeniin, yhtäkkiä edessäsi odottaa vihamielinen luuranko!")
             print ("Taistelu alkakoon!")
             print(f"{luuranko.nimi}, {luuranko.ikä} vuotias, Elämäpisteet: {luuranko.hp}")
             valikko = (input(f"{menu_3} \nMitä seuravaakasi: "))
        elif valikko == "Lyönti" and pelin_tila == 3:
            print("\nHeilautat mahtavaa miekkaasi!")
            pelaaja1.lyönti(luuranko)
            
            print("\nLuuranko lyö takaisin!")
            luuranko.lyönti(pelaaja1)
        
            if pelaaja1.hp < 12 and "Banaani" in inventaario:
                 print("Repussasi taitaa vielä olla Banaani!? Voisiko siitä olla apua..")
            if pelaaja1.hp <= 0:
                     print("\nLuuranko on päihittänyt sinut! Oispa Banaani..\n-The End-") # Lopetus 2/3
                     quit()
            if luuranko.hp <= 0:
                     print("\nHurraaa! Luuranko on päihitetty!\n-The End-") #Lopetus 3/3 
                     quit()
            valikko = (input(f"{menu_3} \nMitä seuravaaksi: "))

        else:
            print("Tuntematon komento!") 
            if pelin_tila == 0:
                        valikko = (input(f"{menu2} \nMitäs seuraavaksi?: "))
            if pelin_tila == 2:
                                   valikko = (input(f"{menu_2} \nMitäs seuraavaksi?: "))
            if pelin_tila == 3:
                        valikko = (input(f"{menu_3} \nMitäs seuraavaksi?: "))
if valikko == "Lopeta":
            print("Peli loppuu")
        

    
    
        
else:
   print("Olet liian nuori!")