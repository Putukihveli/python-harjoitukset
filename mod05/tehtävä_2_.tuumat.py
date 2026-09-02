#Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan kunnes käyttäjä antaa negatiivisen tuumamäärän.
# Sen jälkeen ohjelma lopettaa toimintansa. 1 tuuma = 2,54 cm

tuuma = float(input("Anna tuuma: "))
while tuuma >= 1:
    cm = tuuma * 2.54
    print (f"{tuuma} tuumaa = {cm:2.2f} cm")
    tuuma = float(input("Anna tuuma: "))
if tuuma == 0:
    print(" 0 tuumaa = 0 cm")
else: print (f"{tuuma} on virheellinen tuumamäärä!")
