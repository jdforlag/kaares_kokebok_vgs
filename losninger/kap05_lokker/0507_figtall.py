# De 10 første
prikker_totalt = 0
for fignr in range(1, 11):
    K = fignr**2
    print(f"K_{fignr} = {K}")
    prikker_totalt += K
print("Prikker totalt:", prikker_totalt)

# Antall figurer Pia kan tegne før hun når 3000 prikker
prikker_igjen = 3000
fignr = 1
while prikker_igjen >= fignr**2:
    prikker_igjen -= fignr**2
    fignr += 1
print("Siste figurnummer:", fignr - 1)
