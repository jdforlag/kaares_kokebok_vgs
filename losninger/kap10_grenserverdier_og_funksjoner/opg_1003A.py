import numpy as np
ln = np.log

def f(x):
    return x*ln(x)

a = 1
for i in range(30):  # Gjenta 30 ganger
    print(f(a))      # Skriv ut f(a)
    a = a / 2        # Halver verdien til a

# Utskriften viser at f(a) nærmer seg 0 når a nærmer seg 0 ovenfra.
# Grenseverdien er altså
#     lim (x -> 0+) x*ln x = 0
