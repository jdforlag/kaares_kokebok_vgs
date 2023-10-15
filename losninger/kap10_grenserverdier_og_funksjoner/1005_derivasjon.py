def f(x):
    return x**2 - 4*x - 2

def f_d(x, h=0.0001):
    """Returnerer verdien til f'(x)"""
    return (f(x+h)-f(x)) / h


# La brukeren skrive inn en x-verdi og beregne både f(x) og f'(x) med den nye h-verdien.
a = float(input("Oppgi en x-verdi: "))  # Leser inn en x-verdi fra brukeren
print(f"f(x) = {f(a)}")
print(f"f'(x) = {f_d(a):.3f}")  # Bruker den h-verdien som ga nærmest -4.000 for f'(0)

# Undersøker verdien til den deriverte basert på brukerens input
if f_d(a) > 0:
    print(f"Funksjonen vokser når x = {a}")
elif f_d(a) < 0:
    print(f"Funksjonen minker når x = {a}")
