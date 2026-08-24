print ("Hei, lasketaan suorakulmion piiri sekä pinta-ala!")

kanta = input("Anna suorakulmion kanta: ")
korkeus = input("Anna suorakulmion korkeus: ")
print(f"{'Suorakulmion piiri':9s}:{2*int(kanta) + 2*int(korkeus):0.1f}")
print(f"{'Suorakulmion pinta-ala':9s}:{int(kanta)*int(korkeus):0.1f}")
