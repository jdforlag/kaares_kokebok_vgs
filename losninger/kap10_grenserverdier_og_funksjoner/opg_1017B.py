def f(x):
    return x**x

x = 1.0
for i in range(30):
    print(f"x = {x}, x**x = {f(x)}")
    x = x / 2

# Verdiene nærmer seg 1:
#     lim (x -> 0+) x**x = 1
#
# Forklaring ved regning: x = e**(ln x), og dermed
#     x**x = (e**(ln x))**x = e**(x * ln x)
# Fra oppgave 10.3 vet vi at x*ln x går mot 0, så uttrykket går mot e**0 = 1.
