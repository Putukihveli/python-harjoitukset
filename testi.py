import math
#print(math.fmod(20, 4))
#print(math.fmod(20, 3))
#print(math.fmod(15, 6))
#print(math.fmod(-10, 3)) 

#massi = float(input("anna massit: "))
#if massi >= 7:
#    print ("Sait kahvin: ")
#else: 
#    print(f"{'Lukujen summa':9s}:{int(massi) - int(7):0.0f}")


#ikä = int(input("Anna ikä: "))
#if 15 <= ikä < 18:
#    paino = float(input("Anna paino (kg): "))
#if ikä >= 18 or (ikä >= 15 and paino >= 55):
#    print("Lääkkeen käyttö on sallittua.")   
#else: print("Arvot ei ole kelpoisia")


#ikä = int(input("Anna ikä: "))
#paino = 0
#if 15 <= ikä < 18:
#    paino = float(input("Anna paino (kg): "))
#if (paino >= 55 and ikä >=15 ) or (ikä >= 18):
#    print("Lääkkeen käyttö on sallittua.")
#


#kerrat = int(input("Montako kertaa tervehditään: "))
#tehdyt = 0
#while tehdyt < kerrat:
#    print("Hyvää huomenta")
#    tehdyt = tehdyt + 1

komento = input("Anna komento  : ")
while komento != "lopeta":
    if komento == "MAYDAY":
        break
    print("Suoritan toiminnon: " + komento)
    komento = input("Anna komento: ")
else:
    print("Näkemiin.")
print("Toiminnot lopetettu.")