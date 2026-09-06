import numpy as np

E_Y = 168
SD_Y = 7
N = 10000

antall_hoyere = 0
for _ in range(N):
    hoyde = np.random.normal(E_Y, SD_Y)
    if hoyde >= 182:
        antall_hoyere += 1

sanns = antall_hoyere / N
print(f"P(X >= 182) = {sanns:.3f}")
