x = 3
for i in range(15):
    uttrykk = (4*x**2-x) / (3*x-2*x**2+1)
    print(uttrykk)
    x = x * 10

# Verdiene nærmer seg -2. Grenseverdien er altså
#     lim (x -> uendelig) (4x^2-x)/(3x-2x^2+1) = 4/(-2) = -2
