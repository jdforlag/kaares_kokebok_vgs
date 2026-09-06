import random

def f(x):
    return x**3 - 4*x**2 + 4

x_verdi = random.uniform(-2, 4.5)
f_verdi = f(x_verdi)

# Undersøker fortegnet til funksjonsverdien
if f_verdi > 0:
    print(f"f({x_verdi:.2f}) = {f_verdi:.2f}. Funksjonsverdien er positiv.")
else:
    print(f"f({x_verdi:.2f}) = {f_verdi:.2f}. Funksjonsverdien er negativ.")
