print("Oppgi høyde i cm:")
hoyde = float(input())
if hoyde > 160:
    pris = 280
elif hoyde > 130:
    pris = 210
else:
    pris = 70

print(f"Billettprisen er {pris} kr.")