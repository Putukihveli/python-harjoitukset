inventaario = []
import random
import json


def reppu(kauppa,inventaario):
    haettu_tavara = input ("\nLisätään tavara reppuun:")
    for tuote in kauppa.hylly:
        if str(tuote) == haettu_tavara:
            kauppa.hylly.remove(tuote)
            inventaario.append(tuote)
            print (f"Reppuun lisättiin: {tuote}")
            break 
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
    varusteet_lista = [str(esine) for esine in pelaaja1.inventaario]
    tallennus_data = {
    "pelaaja": pelaaja1.nimi,
    "sijainti": pelaaja1.sijainti,
    "varusteet": varusteet_lista,
}
    with open("Save.json", "w", encoding="utf-8") as tiedosto:
        json.dump(tallennus_data, tiedosto, indent=4, ensure_ascii=False) # Sisentää neljällä välilyönnillä save on helpompilukuisempi. ensure_ascii=False koska json.dump muuntaa muuten kaikki ääkköset taas unicode-koodeiksi.
    with open("Save.json", "r", encoding="utf-8") as tiedosto:
        data_luettu = json.load(tiedosto)
    print(f"Pelaaja: {data_luettu['pelaaja']}")
    print(f"Sijainti: {data_luettu['sijainti']}")
    print(f"Varusteet: {', '.join(data_luettu['varusteet'])}")