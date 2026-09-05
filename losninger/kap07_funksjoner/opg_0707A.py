def maaker(t):
    """Antall måker etter t år, når bestanden avtar med 12 % per år."""
    return 1500 * 0.88**t

aar = 0

# Teller opp ett år av gangen så lenge det er minst 10 måker igjen
while maaker(aar) >= 10:
    aar += 1

print(f"Det tar {aar} år.")
print(f"Da er det {maaker(aar):.1f} måker igjen.")
