import numpy as np

eske = ["rød"]*2 + ["blå"]*3 + ["grønn"]*5
frek = 0
antall_forsok = 4000

for _ in range(antall_forsok):
    kuler = np.random.choice(eske, size=4, replace=False)
    gronne = sum(kuler == "grønn")
    rode = sum(kuler == "rød")

    if gronne >= 3 or rode == 1:
        frek += 1

rel_frek = frek / antall_forsok
print("Relativ frekvens for 'minst 3 grønne eller nøyaktig én rød' inntreffer")
print(f"er omtrent {rel_frek:.4f}")
