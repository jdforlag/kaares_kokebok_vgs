pris = 2_700_000
ek_prosent = 0.15  # ek = egenkapital
ek_minimum = pris * ek_prosent

print(f"Boligen koster {pris} kr.")
ek = int(input("Oppgi din egenkapital i kr: "))

inntekt = int(input("Oppgi årsinntekt: "))
lanebelop = pris - ek

if ek >= ek_minimum and lanebelop < 4 * inntekt:
    print("Du kan få lån")
else:
    print("Du får ikke lån")
    if ek < ek_minimum:
        ek_mangel = ek_minimum - ek
        print(f"Du mangler {ek_mangel} kr i egenkapital.")
