kg = float(input("Oppgi antall kilogram: "))
g = kg * 1000
hg = g / 100
print(f"{kg} kg = {g} g")
print(f"{g} g = {hg} hg")

timer = float(input("Oppgi antall timer: "))
kg_per_time = kg/timer
print(f"Plukkehastigheten er {kg_per_time} kg per time")
minutter = timer * 60
minutter_per_hg = minutter / hg
print(f"Plukkehastigheten er {minutter_per_hg} minutter per hg")
