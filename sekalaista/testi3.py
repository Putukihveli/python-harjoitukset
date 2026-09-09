menu = ("\nvalikko1 \nvalikko2 \nvalikko3 \nvalikko4\n \nVikatilanteissa kokeile 'apua' ")
menu2 = ("\nvalikko1 <- \nvalikko2 <- \nvalikko3 <- \nvalikko4 <-")
nimi = (input("Anna nimesi: "))
ikä = int(input("Anna ikäsi: "))

if ikä >= 12:
    print(f"{nimi}{ikä} - Tervetuloa peliin!")
    print (menu)
    valikko = (input("\nMitäs seuraavaksi: "))
    while valikko != "Lopeta": 
        if valikko == "apua": 
            print("\nValikoista saat avattua valikoita!")
            valikko = (input(f"{menu2}\n \nMitäs seuraavaksi?: "))
        if valikko == "käyttäjä":
            print(f"-{nimi}{ikä}-")
        valikko = (input(f"{menu}\n \nMitäs seuraavaksi: "))
    
    if valikko == "Lopeta":
        print("Peli loppuu")
    

              
elif ikä <= 12:
    print("Olet liian nuori!")