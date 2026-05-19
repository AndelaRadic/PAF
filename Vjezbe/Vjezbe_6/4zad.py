import math
def aritmeticka_sredina(podaci):
    return sum(podaci) / len(podaci)

def standardna_devijacija(podaci):
    sredina = aritmeticka_sredina(podaci)
    suma = 0
    for x in podaci:
        suma += (x - sredina) ** 2
    return math.sqrt(suma / (len(podaci) - 1))

def volumen_valjka(R, L):
    return math.pi * R**2 * L

def sigma_volumena(R, sigma_R, L, sigma_L):
    prvi_dio = (2 * math.pi * R * L * sigma_R) ** 2
    drugi_dio = (math.pi * R**2 * sigma_L) ** 2
    return math.sqrt(prvi_dio + drugi_dio)

def gustoca(m, V):
    return m / V

def sigma_gustoce(m, sigma_m, V, sigma_V):
    prvi_dio = (sigma_m / V) ** 2
    drugi_dio = ((m * sigma_V) / (V ** 2)) ** 2
    return math.sqrt(prvi_dio + drugi_dio)

def odredi_materijal(rho):
    if rho < 3:
        return "Aluminij"
    elif 6 < rho < 9:
        return "Čelik / mesing / bakar"
    else:
        return "Nepoznat"


def obradi_valjak(naziv, promjeri, duljine, mase):
    d = aritmeticka_sredina(promjeri)
    sigma_d = standardna_devijacija(promjeri)

    m = aritmeticka_sredina(mase)
    sigma_m = standardna_devijacija(mase)
    
    L = aritmeticka_sredina(duljine)
    sigma_L = standardna_devijacija(duljine)

    d = d / 10
    sigma_d = sigma_d / 10

    L = L / 10
    sigma_L = sigma_L / 10

    R = d / 2
    sigma_R = sigma_d / 2

    V = volumen_valjka(R, L)
    sigma_V = sigma_volumena(R, sigma_R, L, sigma_L)

    rho = gustoca(m, V)
    sigma_rho = sigma_gustoce(m, sigma_m, V, sigma_V)

    rel_pogreska = sigma_rho / rho

    materijal = odredi_materijal(rho)


    print("\n-------------------")
    print(naziv)
    print("-------------------")

    print(f"Volumen = {V:.3e} cm^3")
    print(f"Sigma volumena = {sigma_V:.3e} cm^3")

    print(f"Relativna pogreška = {rel_pogreska:.3e}")
    print(f"Relativna pogreška (%) = {rel_pogreska*100:.2f}%")

    print("Materijal =", materijal)


    print(f"Gustoća = {rho:.3e} g/cm^3")
    print(f"Sigma gustoće = {sigma_rho:.3e} g/cm^3")

promjeri1 = [19.98, 20.18, 20.10, 20.08, 19.74]
duljine1 = [49.80, 49.00, 50.48, 49.80, 49.96]
mase1     = [138.92, 138.98, 139.20, 138.90, 138.92]

promjeri2 = [19.92, 19.82, 19.96, 19.98, 19.88]
duljine2 = [52.56, 52.50, 52.62, 52.58, 52.54]
mase2     = [128.65, 128.60, 128.65, 128.35, 128.50]

promjeri3 = [24.96, 24.98, 24.98, 24.92, 24.94]
duljine3 = [55.34, 55.40, 55.30, 55.44, 55.48]
mase3     = [71.89, 71.90, 71.79, 71.85, 71.70]

obradi_valjak("Valjak 1", promjeri1, duljine1, mase1)
obradi_valjak("Valjak 2", promjeri2, duljine2, mase2)
obradi_valjak("Valjak 3", promjeri3, duljine3, mase3)
