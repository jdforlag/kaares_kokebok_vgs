import matplotlib.pyplot as plt
import numpy as np

def h(x):
    return 100 * 1.05**x

k = float(input("Oppgi k (0 < k < 50): "))

# Kontrollerer at brukeren har oppgitt en gyldig verdi
if k <= 0 or k >= 50:
    print("Ugyldig verdi. Du må ha 0 < k < 50.")
else:
    # Grafen til h
    x = np.arange(0, 75.01, 0.01)
    plt.plot(x, h(x), label=r"$h(x)=100\cdot 1{,}05^x$")

    # De to punktene på grafen
    x1 = k
    x2 = k + 20
    plt.plot(x1, h(x1), "o", color="red")
    plt.plot(x2, h(x2), "o", color="red")

    # Linjestykket mellom punktene
    plt.plot([x1, x2], [h(x1), h(x2)], color="red", label="Linjestykke")

    # Gjennomsnittlig vekstfart er stigningstallet til linjestykket
    endring_y = h(x2) - h(x1)
    endring_x = x2 - x1
    gvf = endring_y / endring_x
    print(f"Gjennomsnittlig vekstfart i [{x1}, {x2}] er {gvf:.2f}.")

    plt.grid()
    plt.xlabel("x")
    plt.ylabel("h(x)")
    plt.legend()
    plt.show()
