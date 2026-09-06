import numpy as np
antall_forsok = 5000
frek_minst3jenter = 0
for _ in range(antall_forsok):
    # 18 jenter, 12 gutter, 4 trekkes
    jenter_trukket = np.random.hypergeometric(18, 12, 4)
    if jenter_trukket >= 3:
        frek_minst3jenter += 1

relfrek_minst3jenter = frek_minst3jenter / antall_forsok
print(f"P(X>=3) er ca. {relfrek_minst3jenter:.3f}.")
