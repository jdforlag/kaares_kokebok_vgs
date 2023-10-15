# Bredde og høyde til det store rektanglet
bredde = 4
hoyde = 2

# Skriver ut oversikt
print("Antall deler", "Areal del", "Areal hele")
for deler in range(1, 17):  # Antall deler fra 1 til 16
    bredde_del = bredde / deler
    areal_del = bredde_del * hoyde
    areal = areal_del * deler  # Totalareal basert på antall deler og arealet av en del
    print(deler, round(areal_del, 1), areal)
