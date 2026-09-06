from itertools import combinations

ingredienser = ["salat", "tomat", "agurk", "oliven", "feta", "løk"]
salater = list(combinations(ingredienser, 4))

gunstige = 0
for salat in salater:
    print(salat)
    if "tomat" in salat and "løk" in salat:
        print("Både løk og tomat")
        gunstige += 1

mulige = len(salater)
print(f"Antall mulige salater: {mulige}")
print(f"Antall med både tomat og løk: {gunstige}")
print(f"Sannsynligheten er {gunstige}/{mulige} = {gunstige/mulige:.4f}")
