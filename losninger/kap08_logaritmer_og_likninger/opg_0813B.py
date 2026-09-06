def E(M):
    """Energien i joule som blir utløst av et jordskjelv med måltall M."""
    return 10**(M*3/2+22/5)

maltall = float(input("Oppgi måltallet (1-10): "))

energi = E(maltall)          # Energien i joule
energi_MJ = energi / 10**6   # 1 MJ = 10**6 J

print(f"Jordskjelvet utløste {energi_MJ:.1f} MJ.")
print(f"Det er det samme som {energi:.3e} J.")
