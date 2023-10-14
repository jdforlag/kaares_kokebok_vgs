pris_for = 499
endring_pros = float(input("Oppgi endring i prosent: "))
endring_kr = pris_for * endring_pros / 100
pris_etter = pris_for + endring_kr
print(f"Den nye prisen er {pris_etter:.2f} kr.")
