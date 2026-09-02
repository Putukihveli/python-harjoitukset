menu = ("\nvalikko1 \nvalikko2 \nvalikko3 \nvalikko4")
menu2 = ("\nvalikko1 <- \nvalikko2 <- \nvalikko3 <- \nvalikko4 <-")
nimi = (input("Anna nimesi: "))
ikä = int(input("Anna ikäsi: "))
#print (f"Pelaaja: {nimi}{ikä}")
if ikä >= 12:
    print(f"{nimi}{ikä} - Tervetuloa peliin!")
    print (menu)
    valikko = (input("\nMitäs seuraavaksi: "))
    if valikko == "Lopeta": 
        print ("heihei!")
    elif valikko == "apua":
      print("\nValikoista saat avattua valikoita!")
      print(menu2)
      valikko = (input("\nMitäs seuraavaksi: "))
    print (menu)
    if valikko == "aloita alusta":
        print("Aloitetaan alusta")
else:
    print ("Alaikäikäinen, peli sulkeutuu!")









#nimi = (input("Anna nimesi: "))
#ikä = int(input("Anna ikäsi: "))
#print (f"Pelaaja: {nimi}{ikä}")
#while ikä >= 12:
#    print(f"{nimi}{ikä} - Tervetuloa peliin!")
#    print("\nvalikko1 \nvalikko2 \nvalikko3 \nvalikko4")
#    if ikä < 12:
#        break
#    print ("Alaikäikäinen, peli sulkeutuu!")#
#
#if ikä >= 12: 
#    valikko = (input("\nMitäs seuraavaksi: "))
#if valikko == "Lopeta": 
#    print ("heihei!")
