# Konvertering fra kilogram til gram og hektogram
kg = float(input("Oppgi antall kilogram: "))
g = kg * 1000
print(f"{kg} kg = {g} g")
hg = g / 100
print(f"{g} g = {hg} hg")

# Beregning av plukkehastighet og tid per hektogram
timer = float(input("Oppgi antall timer: "))
kg_per_time = kg / timer
print(f"Plukkehastighet: {kg_per_time} kg/t")
minutter = timer * 60
minutter_per_hg = minutter / hg
print(f"Tid per hektogram: {minutter_per_hg} min/hg")