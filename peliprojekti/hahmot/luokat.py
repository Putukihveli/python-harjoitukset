import random
import math
class Humanoidi:
     def __init__(self,nimi, ikä, sijainti=None,):
        self.nimi = nimi
        self.ikä = ikä
        self.paikka = sijainti
        self.hp = 40

     def __repr__(self): 
      return self.paikka, self.nimi
        
     def vaihda_sijaintia(self, uusi_paikka):
         if self.paikka != uusi_paikka:
          self.paikka = uusi_paikka
          print(f"{self.nimi} Siirtyi paikkaan: {uusi_paikka}")

     #def lyönti(self, hahmo):
        # vahinko = random.randint(4,12)
         #luuranko.hp = luuranko.hp - vahinko
         #print(f"Lyöntisi teki {vahinko} vahinkoa!{luuranko.nimi}{luuranko.hp}")
         #return vahinko
     
     def lyönti(self, hahmo): # hahmo parametrilla saatiin muokattua etti lyönti aina osu omaan naamaan
         vahinko = random.randint(4,12)
         hahmo.hp = hahmo.hp - vahinko
         print(f"{self.nimi} Lyönti teki {vahinko} vahinkoa! {hahmo.nimi} Elämäpisteet: {hahmo.hp}") # Tulostetaan lyöjä sekä kohteen tiedot.
         return vahinko

#def kiihdytä(self, kmh):
        #uusi_nopeus = self.nopeus + kmh

        #if uusi_nopeus > self.huippunopeus:
            #self.nopeus = self.huippunopeus
        #elif uusi_nopeus < 0:
            #self.nopeus = 0
        #else:
       #     self.nopeus = uusi_nopeus

        
class Pelaaja(Humanoidi):
    def __init__(self,nimi, ikä, sijainti=None,):
        super().__init__(nimi, ikä, sijainti,)
        self.inventaario = []
        self.hp = 50
    def __repr__(self): 
            return self.paikka

class Esine:
    def __init__(self, nimi, paino,):
        self.nimi = nimi
        self.paino = paino

    def __repr__(self): #tällä pystyy määrittämään miltä olio näyttää listoissa. Jotta kauppiaan "hyllyä" tulostaessa ei näy object at 0x000 blablabla.
        return self.nimi

class Miekka(Esine):
    def __init__(self,nimi,paino,vahinko):
            super().__init__(nimi, paino,)
            self.vahinko = vahinko

    #def __str__(self):
    #    return (f"{self.nimi}, Paino: {self.paino}, Vahinko: {self.vahinko}")

class Reppu(Esine):
    def __int__(self,paino,nimi):
          super().__init__(nimi,paino)
          self.tavarat = []
    #def __str__(self):
        #return(f"Nyssykkä jonne voi lisätä tavaroita!")

class Huone:
    def __init__(self,nimi,valaistus,lämpötila,sijainti):
        self.nimi = nimi
        self.valaistus = valaistus
        self.lämpötila = lämpötila
        self.sijainti = sijainti
        self.tavarat = []
    def __repr__(self): 
            return self.sijainti
    
class Luola(Huone): # onko järkeä luoda luola aliluokkana?
    def __init__(self,nimi,valaistus,lämpötila):
     super().__init__(nimi,valaistus,lämpötila, "Luola")
     self.sijainti = "Luola"

class Kauppa(Huone):
    def __init__(self,nimi,valaistus,lämpötila,sijainti,):
     super().__init__(nimi,valaistus,lämpötila,sijainti)
     self.hylly = ["Banaani", "Kompassi"]
    def lisaa_tuote(self, uusi_tuote): # Luodaan funktio jotta saadaan lisättyä pääkoodin alussa kauppiaan hyllylle miekka ja säkki.
        self.hylly.append() 

