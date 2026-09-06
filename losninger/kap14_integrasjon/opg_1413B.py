# Forklaring:
# Eleven regner ut det bestemte integralet
#     integralet fra 0 til 2 av (x**2 + 2) dx
# Intervallet [0, 2] deles i n = 10 000 like brede rektangler, og høyden av
# hvert rektangel leses av i venstre endepunkt (venstretilnærming).
# Summen av rektangelarealene er en tilnærming til integralet.
#
# Det eksakte svaret:
#     En antiderivert er F(x) = x**3/3 + 2x
#     F(2) - F(0) = 8/3 + 4 = 20/3 = 6,667

def f(x):
    return x**2 + 2

a = 0
b = 2
n = 10000

I = 0
h = (b-a)/n

for i in range(n):
    I = I + f(a+i*h)*h

print(round(I, 3))
print(f"Det eksakte svaret er 20/3 = {20/3:.3f}")
