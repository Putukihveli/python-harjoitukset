#Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina ja palauttaa paluuarvonaan vastaavan litramäärän.
# Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi. Muunnos on tehtävä aliohjelmaa hyödyntäen. 
# Muuntamista jatketaan siihen saakka, kunnes käyttäjä syöttää negatiivisen gallonamäärän.
#Yksi gallona on 3,785 litraa.


def bensiini(gallona):
    return gallona * 3.78

galloni = int(input("anna gallonat: "))
while galloni >= 0:
    print (bensiini(galloni))
    galloni = int(input("anna gallonat: "))
else: 
    print("Virheellinen gallonamäärä")
