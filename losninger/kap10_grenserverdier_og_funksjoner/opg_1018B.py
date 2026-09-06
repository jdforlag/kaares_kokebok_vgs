def g(x):
    return (x**2 - 2*x - 3) / (x - 3)

k = 1.0
x = 3.0 - k  # x nærmer seg 3 nedenfra, altså x -> 3-

for i in range(15):
    print(f"x = {x}, g(x) = {g(x)}")
    k = k / 2
    x = 3.0 - k

# Verdiene nærmer seg 4:
#     lim (x -> 3-) g(x) = 4
#
# Ved regning: x**2 - 2x - 3 = (x-3)(x+1), så g(x) = x + 1 for alle x som
# ikke er 3. Derfor nærmer g(x) seg 3 + 1 = 4.
