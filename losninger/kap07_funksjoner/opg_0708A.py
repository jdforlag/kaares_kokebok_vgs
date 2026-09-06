def p(x):  # Pris per pensjonist ved x pensjonister
    return 40_000 / x + 1500

pens = 1  # Antall pensjonister

# Øker antall pensjonister så lenge prisen er 1800 kr eller mer
while p(pens) >= 1800:
    pens += 1

print(f"Det må være minst {pens} pensjonister.")
print(f"Da blir prisen {p(pens):.2f} kr per pensjonist.")
