def f(x):
    return x**3 - x - 5

def fd(x):  # Numerisk derivert av f
    h = 0.0001
    return (f(x+h) - f(x)) / h

x0 = 2  # Startgjetning i intervallet [0, 4]
x1 = x0 - f(x0)/fd(x0)

# Vi bruker absoluttverdien, slik at kravet gjelder uansett fortegn på f(x1)
while abs(f(x1)) > 10**(-7):
    x0 = x1
    x1 = x0 - f(x0)/fd(x0)

print(f"Løsningen er x = {x1:.6f}")
