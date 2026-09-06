from itertools import permutations

personer = ["Jens", "Knut", "Lars", "Mikael"]
oppstillinger = permutations(personer)

antall = 0
for p in oppstillinger:
    plass_jens = p.index("Jens")
    plass_mikael = p.index("Mikael")

    # De to står ved siden av hverandre når plassnumrene skiller med 1.
    # Vi teller derfor opp de oppstillingene der forskjellen er større.
    if abs(plass_jens - plass_mikael) > 1:
        print(p)
        antall += 1

print(f"Antall oppstillinger der Jens og Mikael ikke står ved siden av hverandre: {antall}")
