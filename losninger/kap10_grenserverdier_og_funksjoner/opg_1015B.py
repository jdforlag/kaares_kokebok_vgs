def h(x):
    return x**2 - 5

def hd(x):  # Numerisk derivert av h
    dx = 0.0001
    return (h(x+dx) - h(x)) / dx

x0 = 4  # Startgjetning
x1 = x0 - h(x0)/hd(x0)

# Newtons metode: hver runde gir en bedre tilnærming
while abs(h(x1)) > 0.001:
    x0 = x1
    x1 = x0 - h(x0)/hd(x0)

print(f"Nullpunktet er x = {x1:.4f}")
print(f"Til sammenligning er kvadratroten av 5 lik {5**0.5:.4f}")
