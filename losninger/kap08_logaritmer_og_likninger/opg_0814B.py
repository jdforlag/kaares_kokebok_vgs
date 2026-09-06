import numpy as np

lg = np.log10

# Vi får vite at løsningen ligger mellom 10 og 100, så vi starter på 10.
x = 10
while x*lg(x) < 150:
    x = x + 1

print(f"x = {x}")

# Vi sammenligner med tallet like under, for å se hvilket heltall
# som ligger nærmest løsningen.
print(f"Kontroll: {x-1} * lg({x-1}) = {(x-1)*lg(x-1):.2f}")
print(f"Kontroll: {x} * lg({x}) = {x*lg(x):.2f}")
print(f"Heltallet {x-1} ligger nærmest, siden 149.91 er nærmere 150 enn 152.25.")
