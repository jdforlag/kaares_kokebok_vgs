# Startverdier
nonstop_figur = 10
nonstop_totalt = 10

# Overskrifter
print("Figurnummer\t\tNon Stop i figur\tNon Stop totalt")

for figurnummer in range(1, 21):
    print(figurnummer, nonstop_figur, nonstop_totalt, sep="\t\t\t")
    nonstop_figur += 4
    nonstop_totalt += nonstop_figur