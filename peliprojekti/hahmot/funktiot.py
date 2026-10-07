inventaario = []
import random
import json
import sys,time


def reppu(kauppa,inventaario):
    haettu_tavara = input ("\nLisätään tavara reppuun:") 
    for tuote in kauppa.hylly:
        if str(tuote) == haettu_tavara:
            kauppa.hylly.remove(tuote)
            inventaario.append(tuote)
            print (f"Reppuun lisättiin: {tuote}")
            if str(tuote) == "Banaani":
                print("\nTämä tulee varmasti tarpeeseen tulevaisuudessa!")
        else: print("Kauppias ei tainnut kuulla mitä sanoit?")
        break

 
def tavarat(inventaario):
    print (f"Repussasi on: {inventaario}")
    return


#def pelaaja_lyönti():
 #   vahinko = random.randint(4,12)
 #   luuranko.hp = luuranko.hp - vahinko
 #   print(f"Lyöntisi teki {vahinko} vahinkoa!")
 #   return vahinko

#def luuranko_lyönti():
 #   vahinko = random.randint(4,12)
  #  print(f"Lyöntisi teki {vahinko} vahinkoa!")
  #  return vahinko


 #def vaihda_sijaintia(self, uusi_paikka):
        # if self.paikka != uusi_paikka:
         # self.paikka = uusi_paikka
         # print(f"{self.nimi} Siirtyi paikkaan: {uusi_paikka}")


def print_slow(str): #dramaattinen tulostus lainattu stackoverflowsta :-D
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.2)

#def vahinko():



def tallenna(pelaaja1):
    varusteet_lista = [str(esine) for esine in pelaaja1.inventaario]
    tallennus_data = {
    "pelaaja": pelaaja1.nimi,
    "sijainti": pelaaja1.paikka,
    "varusteet": varusteet_lista,
}
    with open("Save.json", "w", encoding="utf-8") as tiedosto:
        json.dump(tallennus_data, tiedosto, indent=4, ensure_ascii=False) # Sisentää neljällä välilyönnillä save on helpompilukuisempi. ensure_ascii=False koska json.dump muuntaa muuten kaikki ääkköset taas unicode-koodeiksi.
    with open("Save.json", "r", encoding="utf-8") as tiedosto:
        data_luettu = json.load(tiedosto)
    print(f"Pelaaja: {data_luettu['pelaaja']}")
    print(f"Sijainti: {data_luettu['sijainti']}")
    print(f"Varusteet: {', '.join(data_luettu['varusteet'])}")