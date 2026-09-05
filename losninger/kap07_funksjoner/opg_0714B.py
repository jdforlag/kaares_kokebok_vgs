def f(x):
    return -x**2 + 5*x + 4

steg = 0.01
x = -1

# f vokser helt fram til toppunktet. Når neste funksjonsverdi ikke lenger
# er større enn den vi står i, har vi kommet til toppen.
while f(x) < f(x+steg):  # Så lenge f vokser
    x += steg  # Øk x med steg

print(f"Toppunktet er ({x:.2f}, {f(x):.2f})")
