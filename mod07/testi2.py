#lista = [(1,2,3),(4,5,6),(7,8,9)] #miten saadaan tulostettua listan sisällä olevasta monikost(tuple) numero 9.
#print(lista[2][2]) #lista alkaa 0,1,2 sama pätee tuplen sisällä olevista arvoista.


import math
def lista(luvut):
    return (luvut,luvut2)

luvut = []
luvut2 = []
luku = (input("Anna ensimmäinen luku tai lopeta painamalla Enter: "))
while luku != "":
    luvut.append(int(luku))
    luku = (input("Anna seuraava luku tai lopeta painamalla Enter: "))
    if int(luku) % 2 == 0:
        luvut2.append(int(luku))
print(lista(luvut))
