#komennot = [Lopeta, apua]
menu = ("\nvalikko1 \nvalikko2 \nvalikko3 \nvalikko4")
menu2 = ("\nvalikko1 <- \nvalikko2 <- \nvalikko3 <- \nvalikko4 <-")
nimi = (input("Anna nimesi: "))
ikä = int(input("Anna ikäsi: "))

if ikä >= 12:
    print(f"{nimi}{ikä} - Tervetuloa peliin!")
    print (menu)
    valikko = (input("\nMitäs seuraavaksi: "))
    while valikko != "Lopeta": 
        if valikko == "apua": 
            valikko = (input(f"{menu2}\n \nValikoista saat avattua valikoita!: "))
    valikko = (input(f"{menu}\n \nMitäs seuraavaksi: "))
    
    if valikko == "Lopeta":
        print("Peli loppuu")
    

              
elif ikä <= 12:
    print("Olet liian nuori!")





#while answer != '4':
#
 #   answer = input()
  #  if answer == '4':
   #     print("Great job!")
    #else:
     #   print ("Nope! please try again.")