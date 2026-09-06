def L(t):
    return 460_000*1.035**t

antall_aar = 8
samlet_lonn = 0

for aar in range(antall_aar):
    samlet_lonn += L(aar)

print(f"Samlet lønn de 8 første årene er {samlet_lonn:.2f} kr.")
