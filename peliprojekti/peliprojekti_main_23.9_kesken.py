
import json
import os
import random
import math
from hahmot .luokat import Pelaaja, Humanoidi,Esine,Miekka,Reppu, Huone, Luola, Kauppa
from hahmot import tavarat, reppu, tallenna



#polku = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Save.json")

polku = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Intro.txt")
with open (polku, 'r', encoding="utf-8") as tiedosto:
    data = tiedosto.read()
    print(data)
polku = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Ohjeet.txt")
with open (polku, 'r', encoding="utf-8") as tiedosto:
    data_1 = tiedosto.read()



with open("save.txt", "w") as tiedosto:
    tiedosto.write("Pelaaja pääsi tasolle 2.")


inventaario = []
i = 0


menu = ("\nKauppa \nReppu \nTiedot \nOhjeet\n ")  #\nVikatilanteissa kokeile 'apua'
menu2 = ("\nKauppa <- \nReppu <- \nTeidot <- \nOhjeet <- \n")
nimi = (input("Anna nimesi: "))
ikä_1 = int(input("Anna ikäsi: "))

pelaaja1 = Pelaaja(nimi,ikä_1,"Taverna",)
aloitus = Huone("Taverna","Hämärä","Lämmin","Kaupunki")
kauppias = Kauppa("Kauppa","Kirkas","Lämmin", "Kaupunki")
ase = Miekka("Excalibur", ("5kg"), "4-12.")
laukku = Reppu("Säkki", 5,)
    
if ikä_1 >= 12:
    print(f"\n{nimi}{ikä_1} - Tervetuloa peliin!")
    #print(f"{eteinen.nimi}")

    print (menu)
    valikko = (input("Mitäs seuraavaksi: "))
    while valikko != "Lopeta": 
        if not valikko: #muistutus. if not valikko: on sama kuin, if valikko == "": .The not keyword is a logical operator, and is used to reverse the result of the conditional statement:. -> Normaalist tyhjä str = False. not komento kääntää tämän toisinpäin jolloinka False -> True ja if silmukka etenee.
             print("Et syöttänyt mitään")
             valikko = (input(f"{menu} \nMitäs seuraavaksi: "))
        if valikko == "Ohjeet":
            print(data_1)
            valikko = (input(f"{menu} \nMitäs seuraavaksi: "))
        elif valikko == "apua": 
            print("\nValikoista saat avattua valikoita!")
            valikko = (input(f"{menu2} \nMitäs seuraavaksi?: "))
        if valikko == "Tiedot":
            print (f"\nNimi: {pelaaja1.nimi}{pelaaja1.ikä} \nSijainti: {pelaaja1.sijainti}\nElämäpisteet: {pelaaja1.hp}")
            valikko = (input(f"{menu} \nMitäs seuraavaksi: "))
        if valikko == "Tallenna":
            tallenna(pelaaja1)
            print("Peli tallennettu")
        if valikko == "Kauppa" and len(inventaario) != 4:
            print(f"Saavut kauppaan, kauppa on {kauppias.lämpötila} ja valaistus on {kauppias.valaistus}.\nSijainti: {kauppias.sijainti}")
            print("Kauppias on kuullut tulevasta seikkailustasi. Saat lisätä neljä tuotetta reppuusi!")
            print(f"{ase},\n {laukku}") #Miten saisi tulostettua koko "Kauppiaan ostoslistan ilman että tulee "<function tavarat at 0x000001C065704040>" jne.
            while i <= 3:
                reppu(inventaario)
                i += 1
        if valikko == "Kauppa" and len(inventaario) == 4:
            print(f"Reppusi on täynnä, ehkä voisimmeme palata kauppaan myöhemmin uudestaan?.")
            valikko = (input(f"{menu} \nMitäs seuraavaksi: "))
        
        if valikko == "Reppu":
            tavarat(inventaario)
            valikko = (input(f"{menu} \nMitäs seuraavaksi: "))
        else:
            print("Tuntematon komento!")
            valikko = (input(f"{menu2} \nMitäs seuraavaksi?: "))
           
if valikko == "Lopeta":
            print("Peli Loppuu")
        
else:
    print("Olet liian nuori!")