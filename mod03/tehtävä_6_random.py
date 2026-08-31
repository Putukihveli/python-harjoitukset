import random

#28.8 korjattu tehtävät tunnilla.

#koodi1_str = str(random.randint(0, 999)).zfill(3)
#print(koodi1_str)

koodi_1_osa1 = random.randint(0,9)
koodi_1_osa2 = random.randint(0,9)
koodi_1_osa3 = random.randint(0,9)

koodi_2_osa1 = random.randint(1,6)
koodi_2_osa2 = random.randint(1,6)
koodi_2_osa3 = random.randint(1,6)
koodi_2_osa4 = random.randint(1,6)

koodi1 = str(koodi_1_osa1) + str(koodi_1_osa2) + str(koodi_1_osa3)
print(koodi1)
koodi2 = str(koodi_2_osa1) + str(koodi_2_osa2) + str(koodi_2_osa3) + str(koodi_2_osa4)
print(koodi2)

#k1 = random.randint(1,6)
#k2 = random.randint(1,6)
#k3 = random.randint(1,6)
#k4 = random.randint(1,6)




#print(f"{k1}{k2}{k3}{k4}")







#luku1_str = float(random.randint(0,9))
#luku2_str = float(random.randint(0,9))
#luku3_str = float(random.randint(0,9))