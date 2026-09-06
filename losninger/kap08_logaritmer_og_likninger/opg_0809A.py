def N(p):
    """Verdien av leiligheten etter 25 år, når den årlige veksten er p."""
    return 300_000*(1+p)**25

prosent = 0
while N(prosent) < 2_250_000:
    prosent += 0.1
print(f"{prosent = }")

# Steget 0,1 tilsvarer hele 10 prosentpoeng, så svaret over blir grovt.
# Vi gjentar søket med et mye mindre steg for å få et godt svar:
prosent = 0
while N(prosent) < 2_250_000:
    prosent += 0.0001

print(f"Den gjennomsnittlige årlige veksten var {prosent*100:.2f} %.")
