def f(x):
    return x**3 - 3*x + 1

def fd(x, h=0.0001):
    return (f(x + h) - f(x)) / h

x0 = 2  # Startgjetning

# Skriver ut den opprinnelige gjetningen
print(f"x0 = {x0}, f(x0) = {f(x0)}")

# Første tilnærming
x1 = x0 - f(x0) / fd(x0)
print(f"x1 = {x1}")

# Andre tilnærming
x2 = x1 - f(x1) / fd(x1)
print(f"x2 = {x2}")

# Tredje tilnærming
x3 = x2 - f(x2) / fd(x2)
print(f"x3 = {x3}")

# Fjerde tilnærming
x4 = x3 - f(x3) / fd(x3)
print(f"x4 = {x4}")

# Femte tilnærming
x5 = x4 - f(x4) / fd(x4)
print(f"x5 = {x5}")

# Sjette tilnærming
x6 = x5 - f(x5) / fd(x5)
print(f"x6 = {x6}")