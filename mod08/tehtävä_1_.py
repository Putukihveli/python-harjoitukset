#Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron, jonka jälkeen ohjelma tulostaa sitä vastaavan vuodenajan (kevät, kesä, syksy, talvi). 
# Tallenna ohjelmassasi kuukausia vastaavat vuodenajat merkkijonoina monikkotietorakenteeseen. 
# Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten, että joulukuu on ensimmäinen talvikuukausi.

#kuukaudet = ("tammikuu", "helmikuu","maaliskuu", "huhtikuu","toukokuu","kesäkuu","heinäkuu","elokuu","syyskuu","lokakuu","marraskuu","joulukuu")

vuodenajat = ("Talvi", "Kevät", "Kesä", "Syksy")
jarjestysnumero = int(input("Anna kuukauden numero (1-12): "))

if jarjestysnumero in (12, 1, 2):
    kuukausi = vuodenajat[0]
elif jarjestysnumero in (3, 4, 5):
    kuukausi = vuodenajat[1]
elif jarjestysnumero in (6, 7, 8):
    kuukausi = vuodenajat[2]
elif jarjestysnumero in (9, 10, 11):
    kuukausi = vuodenajat[3]

print(f"{jarjestysnumero}. kuukausi kuuluu vuodenaikaan {kuukausi}.")
