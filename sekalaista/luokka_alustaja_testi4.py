class Koira:

    väri = ""

    def __init__(self, nimi, syntymävuosi, minun_väri, haukahdus="Vuh-vuh"):
        self.nimi = nimi
        self.syntymävuosi = syntymävuosi
        self.haukahdus = haukahdus
        Koira.väri = minun_väri

koira1 = Koira("Muro", 2018, "musta")
#print(Koira.väri)
koira2 = Koira("Rekku", 2022, "ruskea", "Viu viu viu")
print(Koira.väri)
#print(f"Koiria on nyt {Koira.tehty}.")