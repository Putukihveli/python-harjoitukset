def summa(*luvut):
    s = 0
    for l in luvut:
        s += l
    return s

print("Summa on", summa(1, 2, 3))

def tervehdi(tervehdys="Hei", kerrat=1):
    for i in range(kerrat):
        print(tervehdys + " " + str(i+1) + ". kerran")
