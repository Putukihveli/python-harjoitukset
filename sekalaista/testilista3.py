nimet = ["Viivi", "Ahmed", "Pekka", "Olga", "Mary"]
for nimi in nimet:
    print("Moi \n" + nimi + "!") # \n = rivinvaihto.

for nimi in nimet: # Sama kuin for i in range(len(nimet)):
    print(nimi)

# listan tulostaminen silmukassa.
for i in range(10):
    print(i+1) # +1 jotta luku on 1-10 ei 0-10

for i in range(len(nimet)):
    print(nimet[i])

for i in range(1, 11): #11 koska 1, 10 = tulostaa 1-9
    print(i)

for i in range(1,11,2): # Tulostaa kahden välein.
    print(i)   

for i in range (11,1, -2): # Tulostaa takaperin.
    print(i)   


for i in range (11,0, -2): # Tulostaa takaperin, ykkönen tulee mukaan.
    print(i)   
   