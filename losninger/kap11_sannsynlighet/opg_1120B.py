import itertools as it

oyne = list(range(1, 7))  # [1, 2, ..., 6]
mulige = it.product(oyne, repeat=2)  # repeat=2 gir 2 terninger
for m in mulige:
    print(m[0], m[1])

# Med 3 terninger bruker vi repeat=3, og teller opp utfallene som gir 13
mulige3 = it.product(oyne, repeat=3)
antall = 0
for m in mulige3:
    if m[0] + m[1] + m[2] == 13:
        antall += 1

print(f"Antall utfall som gir summen 13: {antall}")
print(f"Sannsynligheten er {antall}/216 = {antall/216:.4f}")
