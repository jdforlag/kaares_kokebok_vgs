pris_for = 499
print(f"En vare koster opprinnelig {pris_for} kr.")
pris_etter = float(input("Oppgi ny pris: "))
pris_diff = pris_etter - pris_for
print(f"Prisforskjellen er {pris_diff} kr.")
prosent_diff = (pris_diff / pris_for) * 100
print(f"Forskjellen er {prosent_diff:.1f} %.")