def p(x):
    return 15 - 2.5*x

def q(x):
    return 0.7*x - 7/3

# Grovt søk: øker a med 0,1 så lenge p(a) er større enn q(a)
a = 0
while p(a) > q(a):
    a += 0.1

print(f"p(a) > q(a) er ikke lenger sant når a = {a:.1f}")

# Finere søk: går ett steg tilbake og bruker mye mindre skritt
a -= 0.1
while p(a) > q(a):
    a += 0.0001

print(f"Skjæringspunktet er ({a:.2f}, {p(a):.2f})")
