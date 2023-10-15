import numpy as np

venner = ["Mia", "Pia", "Bo", "Jo", "Jan"]
N = 15_000  # Antall forsøk
frek = 0

# Gjenta trekningen mange ganger og tell opp antall ganger den spesifikke hendelsen inntreffer
for _ in range(N):
    # Trekker 3 venner uten tilbakelegging
    trekning = np.random.choice(venner, size=3, replace=False)  
    if trekning[0] == "Pia" and trekning[1] == "Bo" and trekning[2] == "Jan":
        frek += 1
    # Alternativt: if list(trekning) == ["Pia", "Bo", "Jan"]:

relfrek = frek / N
print(relfrek)