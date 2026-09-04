#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi
#Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen. 
# Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille argumentiksi reverse=True.
luvut = []

luku =  input("Anna luku: ")

while luku != (""):
    luvut.append(int(luku))
    luku = input("Anna luku tai lopeta painamalla Enter: ")

    luvut.sort(reverse=True)
print(luvut[:5])