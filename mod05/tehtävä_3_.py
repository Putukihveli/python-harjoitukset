#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi. Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.

isoin = 0
pienin = 0

while True:
    luku = str(input("Anna luku: "))
    if (luku == ""):
        break
    else:
        luku = float(luku)
    if luku > isoin:
        isoin = luku
    elif luku < pienin:
        pienin = luku    

print(luku, pienin, isoin)