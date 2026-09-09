#class Koira:
#    pass

#koira = Koira() # Luokasta Koira luodaan olio koira.
#koira.nimi = "Rekku" #
#koira.syntymävuosi = 2022

#print(f"{koira.nimi} on syntynyt vuonna {koira.syntymävuosi}." )

class Koira:
    def __init__(self, nimi, syntymävuosi): # konstruktorin parametrit. nimi ja syntymävuosi.
        self.nimi = nimi
        self.syntymävuosi = syntymävuosi
    

koirat = []

svuosi = 2016
nimi = "a"

for i in range(10): # silmukka menee 10x # koirat lisätään listaan.
    koirat.append(Koira(nimi, svuosi))
    svuosi += 1 # seuraavalla silmukalla vuoden vanhempi koira.
    nimi = chr(ord(nimi) +1 ) #chr -> strng muutetaan characteriksi. ord -> antaa unicode arvon.
for koira in koirat: # tulostetaan koiraoliot listasta.
    print (koira.nimi)
    print (koira.syntymävuosi)
