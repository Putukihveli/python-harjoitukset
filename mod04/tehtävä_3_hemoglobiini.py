

sukupuoli = (input("Anna sukupuoli: "))

if sukupuoli == "Mies":
    hemoglobiini = int(input("Anna hemoglobiini arvosi: "))
    if hemoglobiini >= 195: 
        print("hemoglobiiniarvo on korkea")
    elif hemoglobiini < 134:    
        print("hemoglobiini on alhainen:")
    else:
        print("hemoglobiini on normaali")

if sukupuoli == "Nainen":
    hemoglobiini = int(input("Anna hemoglobiini arvosi: "))
    if hemoglobiini >= 175: 
        print("hemoglobiiniarvo on korkea")
    elif hemoglobiini < 117:    
        print("hemoglobiini on alhainen:")
    else:
        print("hemoglobiini on normaali")




#hemoglobiini = int(input("Anna hemoglobiini arvosi: "))



#Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen ja hemoglobiiniarvon (g/l).
# Ohjelma ilmoittaa, onko hemoglobiiniarvo alhainen, normaali vai korkea.
#
#    Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
#    Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.
