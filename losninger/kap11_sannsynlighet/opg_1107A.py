from numpy.random import choice

krukke = ["hvit"]*2 + ["svart"]*6
frekvens = 0
antall_forsok = 2000

for i in range(antall_forsok):
    trekning = choice(krukke, size=2, replace=False)
    hvite = sum(trekning == "hvit")
    if hvite >= 1:
        frekvens += 1

rel_frekvens = frekvens / antall_forsok
print(f"P(minst én hvit) er omtrent {rel_frekvens:.4f}")

# Ved regning: P(minst én hvit) = 1 - P(begge svarte) = 1 - (6/8)*(5/7) = 13/28
print(f"Den eksakte verdien er 13/28 = {13/28:.4f}")
