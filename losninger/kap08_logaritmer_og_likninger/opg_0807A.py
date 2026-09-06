import numpy as np

ln = np.log

x = 1

# Venstresiden vokser. Vi øker x til den har nådd 30.
while x*ln(x) < 30:
    x = x + 1

print(f"{x = }")
