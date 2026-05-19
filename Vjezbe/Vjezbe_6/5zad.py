import numpy as np 
def sigma_n(x):
    x = np.array(x)
    mean = np.mean(x)
    return np.sqrt(np.sum((x - mean) ** 2) / len(x))

def s(x):
    x = np.array(x)
    mean = np.mean(x)
    return np.sqrt(np.sum((x - mean) ** 2) / (len(x) - 1))

def sigma_mean(x):
    return s(x) / np.sqrt(len(x))

def ispisi(x, naziv):
    print(f"\n--- {naziv} ---")
    print(f"sigma_n   = {sigma_n(x):.6f}")
    print(f"s         = {s(x):.6f}")
    print(f"sigma_x̄  = {sigma_mean(x):.6f}")

promjeri1 = [19.98, 20.18, 20.10, 20.08, 19.74]
duljine1  = [49.80, 49.00, 50.48, 49.80, 49.96]
mase1     = [138.92, 138.98, 139.20, 138.90, 138.92]


promjeri2 = [19.92, 19.82, 19.96, 19.98, 19.88]
duljine2  = [52.56, 52.50, 52.62, 52.58, 52.54]
mase2     = [128.65, 128.60, 128.65, 128.35, 128.50]


promjeri3 = [24.96, 24.98, 24.98, 24.92, 24.94]
duljine3  = [55.34, 55.40, 55.30, 55.44, 55.48]
mase3     = [71.89, 71.90, 71.79, 71.85, 71.70]

print("\n================ VALJAK 1 ================")
ispisi(promjeri1, "Promjer 1")
ispisi(duljine1,  "Duljina 1")
ispisi(mase1,     "Masa 1")

print("\n================ VALJAK 2 ================")
ispisi(promjeri2, "Promjer 2")
ispisi(duljine2,  "Duljina 2")
ispisi(mase2,     "Masa 2")

print("\n================ VALJAK 3 ================")
ispisi(promjeri3, "Promjer 3")
ispisi(duljine3,  "Duljina 3")
ispisi(mase3,     "Masa 3")
