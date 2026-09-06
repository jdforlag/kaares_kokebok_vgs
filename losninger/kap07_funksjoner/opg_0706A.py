def g(x):
    return x**3 - 7*x + 6

# Prøver alle heltallene fra -5 til og med 5
for a in range(-5, 6):
    if g(a) == 0:  # Da er a et nullpunkt
        print(a)
