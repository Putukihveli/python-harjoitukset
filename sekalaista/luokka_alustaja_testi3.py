class Koira:

    tehty = 0 # Staattinen muuttuja! Koirille yhtieen. Määrittää kuinka monta koiraa on tehty.
    # staattinen muuttuja vo iolla esimerkiksi aikaisemman koiran väri?

    def __init__(self, nimi, syntymävuosi, haukahdus="Vuh-vuh"):
        self.nimi = nimi
        self.syntymävuosi = syntymävuosi
        self.haukahdus = haukahdus
        Koira.tehty = Koira.tehty + 1 # staattiseen muuttujaan viitataan luokan nimi.muuttujan nimi + 1
        # voi olla myös Koira.tehty += 1

koira1 = Koira("Muro", 2018)
koira2 = Koira("Rekku", 2022, "Viu viu viu")
print(f"Koiria on nyt {Koira.tehty}.") 