import random
toistot = 0
heitot_yhteensä = 0
while toistot < 100000:

    noppa1 = noppa2 = heitot = 0
    while (noppa1 != 6 or noppa2 != 6):
        noppa1 = random.randint(1,6)
        noppa2 = random.randint(1,6)
        heitot = heitot + 1
    #print(f"Tarvittiin {heitot:d} heittoa.")
    toistot = toistot + 1
    heitot_yhteensä = heitot_yhteensä + heitot

heitot_keskimäärin = heitot_yhteensä/toistot
print(f"Heitot keskimäärin: {heitot_keskimäärin:6.4f}")




noppa1 = noppa2 = heitot = 0
while (noppa1 != 6 or noppa2 != 6):
    noppa1 = random.randint(1,6)
    noppa2 = random.randint(1,6)
    heitot = heitot + 1
print(f"Tarvittiin {heitot:d} heittoa.")

#mitä :d tekee?

#eka = 1
#while eka <= 5:
#    toka = 1
#    while toka <= 5:
#        print(f"{eka} kertaa {toka} on {eka*toka:d}")
#        toka = toka + 1
#    eka = eka + 1