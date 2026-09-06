def S(d, a1=100, n=10):  # Gir S10 der d varierer
    # Summeformelen for en aritmetisk rekke:
    #     S_n = n * (a1 + an) / 2,  der an = a1 + d*(n-1)
    return n * (a1 + a1+d*(n-1)) / 2

okning = 1  # Sparebeløpet øker med 1 krone hver uke
pris_jakke = 1900

while S(okning) < pris_jakke:
    okning += 1  # Øk okning med 1

print(f"Ida må øke sparebeløpet med minst {okning} kr hver uke.")
print(f"Da sparer hun {S(okning):.0f} kr i løpet av 10 uker.")
