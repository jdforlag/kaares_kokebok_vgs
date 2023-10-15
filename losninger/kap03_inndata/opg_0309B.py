innskudd = float(input("Oppgi innskudd i kroner: "))
rente = float(input("Oppgi årlig rente: "))
vekstfaktor = 1 + rente / 100
verdi_etter_10_ar = innskudd * (vekstfaktor ** 10)
print(f"Verdien etter 10 år er {verdi_etter_10_ar:.2f} kr.")
