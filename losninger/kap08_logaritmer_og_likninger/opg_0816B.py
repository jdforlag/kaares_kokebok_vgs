def f(x):
    """Forventet levealder for menn født x år etter 1988."""
    return 73.028 * 1.003**x

x = 0

# Levealderen vokser. Vi teller opp til modellen gir 85 år.
while f(x) < 85:
    x += 1

print(f"Det tar {x} år.")
print(f"Menn født i {1988 + x} har en forventet levealder på 85 år.")
