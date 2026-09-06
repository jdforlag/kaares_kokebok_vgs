def f(x):
    """Antall gårdsbruk i Norge x år etter 1999."""
    return 68_900 * 0.982**x

x_verdi = 0
grense = f(0) * 0.60  # 40 prosent lavere enn 1999

# Teller opp ett år av gangen så lenge vi er over grensa
while f(x_verdi) > grense:
    x_verdi += 1

print(f"Det tar {x_verdi} år.")
print(f"Det skjer i år {1999 + x_verdi}.")
