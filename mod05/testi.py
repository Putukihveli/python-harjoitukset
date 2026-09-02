käyttäjä = input("Anna käyttäjätunnus: ")
salasana = input("Anna salasana: ")

kysytty = 0


while käyttäjä != "python" or salasana != "rules":
    print("väärä")
    käyttäjä = input("Anna käyttäjätunnus: ")
    salasana = input("Anna salasana: ")
    if input == 5: 
        print("Pääsy evätty")
else:
    print ("Tervetuloa")