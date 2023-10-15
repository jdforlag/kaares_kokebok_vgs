import numpy as np

ln = np.log

def vs(x):
    return (ln(x))**2 - 4*ln(x)

print(vs(1))
print(vs(15))

i = 15
while vs(i) < 5:
    i += 0.001

print(i)  # 148.414...
