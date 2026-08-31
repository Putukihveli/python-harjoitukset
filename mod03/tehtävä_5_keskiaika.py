#korjattu tunnilla kun tehtävät on tarkistettu.

import math

Leiviskä = float(input("Anna leiviskät: "))
Naula = float(input("Anna naulat: "))
Luoti = float(input("Anna luodit: "))

luoti_grammoina = Luoti * 13.3
naula_grammoina = Naula * 32 * 13.3
leiviskä_grammoina = Leiviskä * 20 * 32 * 13.3

yhteisgrammat = luoti_grammoina + naula_grammoina + leiviskä_grammoina

kilogrammat = int(yhteisgrammat // 1000)
grammat = yhteisgrammat % 1000

print("\nMassa nykymittojen mukaan:")
print(f"{kilogrammat} kilogrammaa ja {grammat:2.0f} grammaa.")



#Yksi leiviskä on 20 naulaa.
#Yksi naula on 32 luotia.
#Yksi luoti on 13,3 grammaa.