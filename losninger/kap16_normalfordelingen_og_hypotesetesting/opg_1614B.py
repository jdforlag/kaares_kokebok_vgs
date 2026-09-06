import numpy as np

elever = 323*["jente"] + 301*["gutter"]

antall_forsok = 10_000
frekvens = 0

for i in range(antall_forsok):
    kjonn = np.random.choice(elever)

    if kjonn == "jente":
        # Trekk høyden fra X
        hoyde = np.random.normal(168, 6)
    else:
        # Trekk høyden fra Y
        hoyde = np.random.normal(180, 8)

    if hoyde > 175:
        frekvens += 1

print(f"P(høyde > 175 cm) er omtrent {frekvens/antall_forsok:.4f}")
