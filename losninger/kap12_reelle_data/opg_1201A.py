jordskjelvene = [15, 25, 10, 4, 6, 9, 11]

maks_skjelv = 0
for jordskjelv in jordskjelvene:
    if jordskjelv > maks_skjelv:
        maks_skjelv = jordskjelv

print(f"Det største antallet jordskjelv på ett år var {maks_skjelv}.")
