import numpy as np

E_X = 3.2
SD_X = 0.8

karakterer = np.random.normal(E_X, SD_X, size=200)
minst5 = 0

for kar in karakterer:
    if kar >= 5.0:
        minst5 += 1

print(minst5)
