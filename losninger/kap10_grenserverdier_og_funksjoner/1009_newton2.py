def f(x):
    return x**5 - 2*x**4 - 3*x**3 + 2*x**2 

def fd(x):
    return 5*x**4 - 8*x**3 - 9*x**2 + 4*x  

x0 = 3  # Prøv også 2 og 0.2 
x1 = x0 - f(x0) / fd(x0)

while abs(f(x1)) > 0.0001:
    x0 = x1
    x1 = x0 - f(x0) / fd(x0)

print(x1)
