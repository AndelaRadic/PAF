import math
class Valjak:
    def __init__(self, naziv, promjeri, duljine, mase):
        self.naziv = naziv
        self.promjeri = promjeri
        self.duljine = duljine
        self.mase = mase

    def aritmeticka_sredina(self, podaci):
        return sum(podaci) / len(podaci)

    def standardna_devijacija(self, podaci):
        sredina = self.aritmeticka_sredina(podaci)
        suma = 0
        for x in podaci:
            suma += (x - sredina) ** 2
        return math.sqrt(suma / (len(podaci) - 1))

    def ispisi_rezultate(self):
        print("\n", self.naziv)
        print("Srednji promjer:", self.aritmeticka_sredina(self.promjeri))
        print("Std dev promjera:", self.standardna_devijacija(self.promjeri))
        print("Srednja duljina:", self.aritmeticka_sredina(self.duljine))
        print("Std dev duljine:", self.standardna_devijacija(self.duljine))
        print("Srednja masa:", self.aritmeticka_sredina(self.mase))
        print("Std dev mase:",  self.standardna_devijacija(self.mase))

valjak1 = Valjak(
    "Valjak 1",
    [19.98, 20.18, 20.10, 20.08, 19.74],
    [49.80, 49.00, 50.48, 49.80, 49.96],
    [138.92, 138.98, 139.20, 138.90, 138.92]
)

valjak2 = Valjak(
    "Valjak 2",
    [19.92, 19.82, 19.96, 19.98, 19.88],
    [52.56, 52.50, 52.62, 52.58, 52.54],
    [128.65, 128.60, 128.65, 128.35, 128.50]
)

valjak3 = Valjak(
    "Valjak 3",
    [24.96, 24.98, 24.98, 24.92, 24.94],
    [55.34, 55.40, 55.30, 55.44, 55.48],
    [71.89, 71.90, 71.79, 71.85, 71.70]
)
valjak1.ispisi_rezultate()
valjak2.ispisi_rezultate()
valjak3.ispisi_rezultate()
    