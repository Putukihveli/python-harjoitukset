inventaario = []
import random
import json


def reppu(inventaario):

    tavara = input ("\nLisätään tavara reppuun:")
    if tavara:
        inventaario.append(tavara)
        print (f"Reppuun lisättiin: {tavara}")

def tavarat(inventaario):
    print (f"Repussasi on: {inventaario}")
    return


def lyönti():
    if Miekka == True:
        print(f"Lyöntisi teki {vahinko} vahinkoa!")
        vahinko = random.randint(4,12)
        if Miekka == False:
            print("Et voi lyödä ilman miekkaa!")

def tallenna(pelaaja1):
    tallennus_data = {
    "pelaaja": pelaaja1.nimi,
    "sijainti": pelaaja1.sijainti,
    "varusteet": pelaaja1.inventaario,
}
    with open("Save.json", "w", encoding="utf-8") as tiedosto:
        json.dump(tallennus_data, tiedosto)
    with open("Save.json", "r", encoding="utf-8") as tiedosto:
        data_luettu = json.load(tiedosto)
    print(f"Pelaaja: {data_luettu['pelaaja']}, sijainti: {data_luettu['sijainti']}, varusteet: {data_luettu['inventaario']}")