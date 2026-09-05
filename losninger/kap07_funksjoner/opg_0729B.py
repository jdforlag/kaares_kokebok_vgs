def V(x):
    """Antall liter vann som er tappet ut x minutter etter at tappingen startet."""
    return 2000 - 2000*(1 - x/40)**2

okninger = []
for i in range(0, 40):
    # Regn ut økningen i V fra x=i til x=i+1
    okning = V(i+1) - V(i)
    okninger.append(okning)

maks_okning = max(okninger)
print(f"Den største økningen i løpet av ett minutt er {maks_okning:.2f} liter.")

if maks_okning > 105:
    print("Det blir tappet ut mer enn 105 liter i løpet av ett minutt.")
else:
    print("Det blir aldri tappet ut mer enn 105 liter i løpet av ett minutt.")
