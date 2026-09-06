def p(n):
    """Økningen i pingvinbestanden i måned nr. n."""
    return 2800 * 1.08**n

total_okning = 0

# Legger sammen økningen for hver av de 12 månedene
for n in range(1, 13):
    total_okning += p(n)

print(f"Den totale økningen dette året er {total_okning:.0f} pingviner.")
