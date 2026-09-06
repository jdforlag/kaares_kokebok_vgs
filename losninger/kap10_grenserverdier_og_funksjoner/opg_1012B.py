def p(n):
    """Verdens populasjon etter n år, med 5 % vekst per år og 2 til å begynne med."""
    return 2 * 1.05**n

aar = 0
while p(aar) < 9_000_000_000:
    aar += 1

print(f"Det tar {aar} år før populasjonen når 9 milliarder.")
print(f"Etter {aar} år er populasjonen {p(aar):.0f}.")
