# Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi. 
# Ohjelma kysyy käyttäjältä, haluaako tämä syöttää uuden lentoaseman, hakea jo syötetyn lentoaseman tiedot vai lopettaa. 
# Jos käyttäjä valitsee uuden lentoaseman syöttämisen, ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen. 
# Jos käyttäjä valitsee haun, ohjelma kysyy ICAO-koodin ja tulostaa sitä vastaavan lentoaseman nimen. 
# Jos käyttäjä haluaa lopettaa, ohjelman suoritus päättyy. 
# Käyttäjä saa valita uuden toiminnon miten monta kertaa tahansa aina siihen asti, kunnes hän haluaa lopettaa. 
# (ICAO-koodi on lentoaseman yksilöivä tunniste. Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK. Löydät koodeja helposti selaimen avulla.)

lentoasemat =  [{"asema": "Helsinki-Vantaa",
                 "ICAO": "EFHK"}]



valinta = input("Haluatko etsiä tiedossa olevaa asemaa, vai antaa uuden? (Etsi / Uusi / Lopeta)")
if valinta == "Lopeta":
     print("Heippa")
while valinta != "Lopeta":
    if valinta == "Uusi":
        asema = input("Anna aseman nimi: ")
        ICAO = input("Anna ICAO koodi: ")
        uusi_asema = {'asema': asema, 'ICAO': ICAO}
        lentoasemat.append(uusi_asema)
        valinta = input("Haluatko etsiä tiedossa olevaa asemaa, vai antaa uuden? (Etsi / Uusi / Lopeta)")
    if valinta == "Etsi":
         haku = input("Anna aseman ICAO koodi:")
    for kenttä in lentoasemat:
        if kenttä ["ICAO"] == haku:
            print(f"Koodia {haku} vastaava kenttä on {kenttä['asema']}.")
            valinta = input("Haluatko etsiä tiedossa olevaa asemaa, vai antaa uuden? (Etsi / Uusi / Lopeta)")

if valinta == "Lopeta":
    print("Poistutaan lentokenttähakujutusta.")
