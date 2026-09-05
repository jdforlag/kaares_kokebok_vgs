def s(p):
    """
    Beregner saldoen for 23 år siden når renten per år er p prosent.
    """
    return 15_000 * (1+p)**(-23)

p = 0

# Jo høyere rente, desto mindre måtte Siri sette inn for 23 år siden.
# Vi øker renta til saldoen for 23 år siden er nede i 8500 kr.
# Jo mindre steg vi bruker, desto mer nøyaktig blir renta.
while s(p) > 8500:
    p += 0.00001

print(f"Den årlige renta var {p*100:.2f} %.")
print(f"Kontroll: For 23 år siden sto det {s(p):.0f} kr på kontoen.")
