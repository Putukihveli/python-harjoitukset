import random
import math
class Humanoidi:
     def __init__(self,nimi, ikä, sijainti=None,):
        self.nimi = nimi
        self.ikä = ikä
        self.sijainti = sijainti
        self.hp = 30

class Pelaaja(Humanoidi):
     def __init__(self,nimi, ikä, sijainti=None,):
        super().__init__(nimi, ikä, sijainti,)
        self.inventaario = []
        self.hp = 50


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
    def __init__(self,nimi,valaistus,lämpötila,sijainti,):
        self.nimi = nimi
        self.valaistus = valaistus
        self.lämpötila = lämpötila
        self.sijainti = sijainti
        self.tavarat = []

class Luola(Huone):
    def __init__(self,nimi,valaistus,lämpötila):
     super().__init__(nimi,valaistus,lämpötila)
     self.sijainti = "Maan alla"

class Kauppa(Huone):
    def __init__(self,nimi,valaistus,lämpötila,sijainti,):
     super().__init__(nimi,valaistus,lämpötila,sijainti)
     self.hylly = ["Banaani", "Kompassi"]
    def lisaa_tuote(self, uusi_tuote):
        self.hylly.append()

