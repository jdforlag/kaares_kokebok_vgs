tall1 = float(input("Oppgi det første tallet: "))
tall2 = float(input("Oppgi det andre tallet: "))
if tall1 < tall2:
    print(f"Det minste tallet er {tall1}")
elif tall2 < tall1:
    print(f"Det minste tallet er {tall2}")
else:
    print("Tallene er like")