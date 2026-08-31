print ("Anna kolmea lukua, saat näiden summan, tulon sekä keskiarvon.")

yksi = input("Anna ensimmäinen luku: ")
kaksi = input("Anna toinen luku: ")
kolme = input("Anna kolmas luku: ")

print(f"{'Lukujen summa':9s}:{int(yksi) + int(kaksi) + int(kolme):0.0f}")
print(f"{'Lukujen tulo':9s}:{int(yksi)*int(kaksi)*int(kolme):0.0f}")
print(f"{'Lukujen keskiarvo':9s}:{(int(yksi)+int(kaksi)+int(kolme)) /3 :0.1f}")



#

summa = yksi + kaksi + kolme
tulo = yksi * kaksi * kolme
keskiarvo = summa / 3

print(f"lukujen summa: {summa}")




