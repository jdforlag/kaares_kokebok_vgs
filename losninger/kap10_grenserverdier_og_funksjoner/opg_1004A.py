def f(x):
    return (3 - x) / (x**2 - 1)

# NB: f er ikke definert for x = 1, siden nevneren blir 0 der.
# Derfor starter vi på 0.5 i stedet for 4.0, slik at halveringene
# aldri treffer x = 1.
a = 0.5
while a > 0.000001:
    print(f"x = {a}, f(x) = {f(a)}")
    a = a / 2

# f(x) nærmer seg -3 når x nærmer seg 0 ovenfra:
#     lim (x -> 0+) (3-x)/(x**2-1) = 3 / (-1) = -3
