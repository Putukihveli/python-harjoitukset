#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi. 
#Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.

luku1 = input("Anna luku: ")
if luku1 == "":
    print("Anna luku:")
else:
    luku = float(luku1)
    isoin = luku
    pienin = luku

    while True:
        luku2 = input("Anna luku: ")
        if luku2 == "":
            break

        luku = float(luku2)

        if luku > isoin: 
            isoin = luku
        if luku < pienin:
            pienin = luku

    print(f"Pienin luku: {pienin}")
    print(f"Isoin luku: {isoin}")