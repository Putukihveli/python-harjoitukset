#with open("save.txt", "r") as tiedosto:
#    data = tiedosto.read()
#    print(data)

import json

tallennus_data = {
    "pelaaja": "Matti",
    "taso": 5,
    "varusteet": ["miekka", "kilpi", "haarniska"]
}

with open("save.json", "w") as tiedosto:
    json.dump(tallennus_data, tiedosto)


with open("save.json", "r") as tiedosto:
    data_luettu = json.load(tiedosto)

print(f"Pelaaja: {data_luettu['pelaaja']}, taso: {data_luettu['taso']}, varusteet: {data_luettu['varusteet']}")

#with open("save.txt", "w") as tiedosto:
# #   tiedosto.write("taso:2")
