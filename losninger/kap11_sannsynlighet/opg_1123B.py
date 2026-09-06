from itertools import combinations

kolleger = ["Sven", "Ole", "Magnus", "Jens", "Kaare"]

luksushytter = list(combinations(kolleger, 2))
gunstige = 0

for luksushytte in luksushytter:
    print(luksushytte)
    # Sven skal være med, og Magnus skal ikke være med
    if "Sven" in luksushytte and "Magnus" not in luksushytte:
        print("Sven i luksushytte, Magnus i vanlig hytte")
        gunstige += 1

mulige = len(luksushytter)
print(f"Antall mulige par: {mulige}")
print(f"Antall gunstige: {gunstige}")
print(f"Sannsynligheten er {gunstige}/{mulige} = {gunstige/mulige:.4f}")
