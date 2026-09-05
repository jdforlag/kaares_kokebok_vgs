def f(x):
    return 1/x + 0.01*x

# Med steg = 0,01 får vi svaret 3.82 < x < 26.19.
# Ved å gjøre steget mindre kommer vi nærmere den korrekte løsningen.
steg = 0.0001

i = 0.1

# Øker i så lenge f(i) er for stor. Første i som gir f(i) < 0,3 blir x1.
while f(i) >= 0.3:
    i += steg
x1 = i

# Fortsetter så lenge f(i) er under 0,3. Første i som gir f(i) >= 0,3 blir x2.
while f(i) < 0.3:
    i += steg
x2 = i

print(f"{x1:.2f} < x < {x2:.2f}")

# Fasit fra GeoGebra: 3.8197 < x < 26.1803
