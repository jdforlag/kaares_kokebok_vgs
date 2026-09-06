x = 3
for i in range(10):
    brok = (x**3-8) / (x**2-4)
    print(brok)
    x = (x+2) / 2  # x nærmer seg 2 ovenfra

# Verdiene nærmer seg 3. Grenseverdien er altså
#     lim (x -> 2) (x^3-8)/(x^2-4) = 3
